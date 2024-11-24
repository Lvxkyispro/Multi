# 🌟 Multi-Purpose Telegram Bot

<p align="center">
  <img src="https://i.imgur.com/ojgXrso.png" alt="Bot Logo" width="150"/>
</p>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![Telegram Bot API](https://img.shields.io/badge/Telegram-Bot%20API-blue)](https://core.telegram.org/bots)  
[![Contributions welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)

</div>

---

## 🚀 About the Project

**Multi-Purpose Telegram Bot** is a flexible and feature-rich bot built in Python. From generating BINs and managing credit card-related data to performing Google searches and image lookups, the bot offers various tools to assist users. It is easy to set up, extend, and customize!  

This bot caters to multiple purposes, including:
- 🌐 Internet tools (search queries, Wikipedia, and image lookups)
- 💳 Card-related tasks (BIN lookup, card generation, cleaning data)
- 📁 File operations (merging, splitting, filtering)
- 🎨 AI and image generation
- 📡 Account and proxy management tools  

---

## 💡 Features

### 🛠️ Core Functionalities

#### 💳 Card & BIN Utilities
- `/bin <number>`: Perform **BIN lookups** to get detailed card issuer data (type, country, etc.)
- `/gbin <amount>`: Generate random **BIN numbers**
- `/gen <bin>`: Generate valid cards based on a **BIN**
- `/gb <brand> <amount>`: Get random **brand-specific BINs**
- `/clean`: Format and validate stolen card dumps

#### 🔍 Internet Tools
- `/search <query>`: Perform **Google searches**
- `/wiki <query>`: Lookup topics directly from **Wikipedia**
- `/ip <address>`: Get location and information tied to an **IP address**
- `/img <query>`: Return relevant images from free APIs

#### 🎨 AI Features
- `/ai <prompt>`: Generate AI-created custom images based on the specified prompt

#### 📁 File Utilities
- `/merge`: Combine multiple text files into one
- `/split <n>`: Divide large files into chunks of size `n`
- `/aflt`: Filter sensitive combinations like email:pass files.

#### 🔐 Proxy and Authentication
- `/crunchy`: Crunchyroll **account verification**
- `/px <connection>`: Test proxies for security and speed 

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.8+
- A valid [Telegram Bot API key](https://core.telegram.org/bots)  
- Optional: A Google API key (for `/search`, `/img`, etc.)  
- Clone the repo:
  ```bash
  git clone https://github.com/lvxkyispro/multi.git
  cd multi
