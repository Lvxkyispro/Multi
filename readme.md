🤖 Multi-Purpose Telegram Bot

This project is a powerful and versatile Telegram bot built with Python's TeleBot library. It offers a variety of features like BIN lookup, card generation, file operations, image generation, IP lookup, search functionality, account checking, and much more.

🚀 Features

📌 Core Commands
/start - Welcome users with a custom greeting message and provide instructions.
/cmds - List all available commands.
/ping - Test bot responsiveness and measure latency.
/reset - Restart the bot if necessary.

💳 BIN and Card Utilities
/bin  - Lookup details about the provided BIN (Bank Identification Number).
/gbin  - Generate random BINs (limit up to 100).
/gen  - Generate valid credit card information from a BIN.
/clean - Clean and standardize credit card data from text files.

🔐 Account Checking
/crunchy - Check individual Crunchyroll combo validity.
/mcrunchy - Bulk check Crunchyroll combos by uploading .txt files.
/gethits  - Retrieve good and premium accounts along with the results from previous checks.

🌐 Search and Information
/search  - Perform a Google search and return top results.
/wiki  - Perform a Wikipedia search and return summarized information.
/data  - Fetch info and images based on person/topic via Google and Wikipedia APIs.

🌍 IP Address Utilities
/ip  - Perform an IP lookup, return location, organization, and privacy (VPN/proxy/tor usage) details.

🧹 File Operations
/split  - Split .txt files into smaller parts (e.g., split 5 divides it into 5 parts).
/merge - Merge multiple .txt files into a single file.
/txt  - Create and upload a .txt file with the given text.
/aflt - Filter email:pass format from files.

🌠 AI and Image Generation
/ai  - Generate AI images based on the given prompt.
/img  - Fetch and return up to 4 images using Google Image Search by query.

🕸️ Proxy Validator
/px  - Check the validity of a proxy formatted as host:port:username:password.

🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/your-repo/multi-purpose-bot.git
cd multi-purpose-bot

2. Install Dependencies

Ensure you have Python 3.8+ installed, then install the required Python libraries:

pip install -r requirements.txt

3. Configure API Keys and Bot Token

Replace placeholders in the script with your actual credentials:

Telegram bot token (from https://t.me/BotFather)
IPInfo API Token** for IP lookups
Google API Key* and *Custom Search Engine ID** for Google Search and Images

4. Run the Bot

python bot.py

📋 Usage Examples

Welcome Message
/start

The bot sends a custom welcome message with a user mention.

BIN Utilities
BIN Lookup:
/bin 457173
Returns BIN info like brand (Visa/MasterCard), issuer, country, and type (credit/debit).

Generate Random BINs:
/gbin 10
Generates up to 10 random BINs.

Generate Cards From BIN:
/gen 457173
Generates 10 valid cards in the format CC|MM|YY|CVV.

Crunchyroll Account Checkers
Single Check:
/crunchy email:password
Returns validity, subscription status (premium/free), plan, and payment method.

Bulk Check:
Reply to a .txt file containing email:password combos:
/mcrunchy

Image and AI Utilities
AI Image Generation:
/ai futuristic cityscape at sunset
Generates an AI-generated image based on the prompt.

Fetch Images From Google:
/img cute cats
Returns 1-4 images for the query cute cats.

File Operations
Merge Files:
Reply .txt files to /merge. After sending all files, use:
/done

Split a Large File:
Reply to a .txt file with:
/split 5
Splits the file into 5 smaller parts.

Create a .txt File:
/txt Your text goes here!
Creates and uploads a .txt file with the provided content.

IP Lookup
Perform an IP address lookup:
/ip 8.8.8.8
Returns location, ISP, and privacy details (VPN/tor/proxy checks).

Search Tools
Google Search:
/search Python programming
Provides top Google search results for the query.

Wikipedia Search:
/wiki Albert Einstein
Returns a brief summary from Wikipedia on the topic.

Detailed Info:
/data Elon Musk
Returns detailed info and an image (when available).

🌟 Key Features

BIN Tools**: Lookup BIN info and generate cards.
Crunchyroll Combo Checker**: Validate individual or bulk combos for subscription and plan details.
Google Integration**: Search the web and fetch images directly in Telegram.
AI Image Generation**: Generate stunning visuals from text prompts.
IP Tools**: Get detailed info on IP addresses.
File Management**: Split, merge, or create .txt files.
Proxy Validator**: Check proxy effectiveness.
Custom Commands**: Personalized responses tailored to user needs.

⚙️ Project Structure

Code Overview
TeleBot Library**: Facilitates Telegram bot functionality.
Google Custom Search API**: For web and image searches.
Requests Library**: API calls and data fetching.
Wikipedia API**: Simplifying access to Wikipedia information.

Modular Structure
The bot is organized into commands, each handling a specific task. Commands are decorated with @bot.message_handler. Functions are reused wherever possible to ensure maintainability.

🛡️ Security Note

While using this bot:
Ensure your API keys and bot tokens are stored securely.
Avoid sharing your token or deploying the bot publicly without restrictions.

This bot’s functionality is for educational purposes only. Use responsibly within the scope of applicable laws.

📜 License

This project is released under the https://opensource.org/licenses/MIT.

🤝 Contributing

Contributions are welcome! Feel free to:
Report bugs or request features by creating an issue.
Submit pull requests with your enhancements or fixes.

💡 Author Info

Developed with ❤️ by [YourName].
Telegram Support**: https://t.me/your_username
GitHub**: https://github.com/your-repo

If you find this project helpful, give it a ⭐ and share it with others!
