# GG.deals Discounts Bot

A Telegram bot built with **Python** and **aiogram** that parses 100% discounts from [GG.deals](https://gg.deals/) and delivers them directly to users.

## Features
- Fetches the latest game discounts from GG.deals (Steam and other platforms).
- Sends automatic discount notifications to Telegram users.
- Stores user data and query history in a local database.

## Tech Stack
- Python 3.10+
- aiogram — Telegram Bot API framework
- Undetected chromedriver(request installed Google Chrome)
- SQLite — lightweight database for storage

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/ggdeals-bot.git
   cd ggdeals-bot
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Create a .env file with your bot token:
   ```bash
   BOT_TOKEN=your_telegram_bot_token
4. Run the bot: 
   ```bash
   python bot.py
