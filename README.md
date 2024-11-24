
🤖 Multi-Purpose Telegram Bot

A versatile Telegram bot built with Python that offers various utilities including BIN checking, card generation, file operations, search functionality, and more.

🌟 Key Features

💳 Card & Payment Tools
/bin  - Check BIN information
/gbin  - Generate random BINs (max 100)
/gen  - Generate valid cards from BIN
/gb   - Generate brand-specific BINs
/clean - Format and clean credit card data

📁 File Operations
/merge - Combine multiple text files
/split  - Split text files into parts
/aflt - Filter email:pass combinations
/txt  - Create text files

🔍 Search & Information
/search  - Google search
/data  - Get detailed information
/wiki  - Wikipedia search
/ip  - IP address lookup
/img  - Image search

🎨 AI Features
/ai  - Generate AI images

🔐 Account Checking
/crunchy - Check Crunchyroll accounts
/mcrunchy - Bulk check Crunchyroll accounts
/px - Check proxy status

🛠️ Installation

Clone the repository:bash
git clone

Install required packages:bash
pip install -r requirements.txt

Configure environment variables:env
BOT_TOKEN=your_telegram_bot_token
GOOGLE_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_search_engine_id
IPINFO_TOKEN=your_ipinfo_token

📋 Dependencies
python-telegram-bot
requests
wikipedia-api
google-api-python-client

🚀 Usage

Start the bot:bash
python pro.py

In Telegram, start a chat with the bot using the /start command

💡 Command Examples

BIN Lookup
/bin 123456

Generate Cards
/gen 123456

Search Images
/img nature sunset

Generate AI Image
/ai cyberpunk city at night

🔒 Security Features
Rate limiting on certain commands
Maximum limits for bulk operations
Error handling for invalid inputs
Secure file handling

🔄 Process Management
/reset - Restart the bot
/ping - Check bot status
Stop functionality for long-running processes

⚠️ Important Notes
API rate limits apply
Some features require specific API keys
File operations have size limitations
Temporary files are automatically cleaned up

🛡️ Error Handling
Input validation
API error handling
File operation safeguards
Network request timeouts

🔧 Maintenance
Regular cleanup of temporary files
Process monitoring
Resource usage optimization

👨‍💻 Development
Written in Python 3.x
Modular code structure
Extensive error handling
Clean code practices

📝 License
MIT License

Copyright (c) 2024 lucky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 

🤝 Contributing
Fork the repository
Create a feature branch
Commit changes
Push to the branch
Create a pull request

🙏 Credits
Telegram Bot API
Google Custom Search API
IPInfo API
Various open-source libraries

📞 Support
For support, join our Telegram channel or create an issue in the repository.

Made with ❤️ by [Your Name]
