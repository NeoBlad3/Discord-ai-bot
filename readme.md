1. Clone the Repo
git clone https://github.com/NeoBlad3/Discord-ai-bot
cd discord-ai-bot

2. Install Dependencies
pip install -r requirements.txt

3. Get API Keys

Discord Bot Token → Discord Developer Portal

OpenAI API Key → OpenAI Dashboard

4. Configure

Edit bot.py and replace:

DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"


(Pro tip: you can also use environment variables for security)

5. Run the Bot
python bot.py

💬 Usage

In any Discord server where your bot is invited:

/ask How do I cook pasta?


👉 Bot replies with an AI-generated answer.

📦 Repo Structure
discord-ai-bot/
│── bot.py              # Main bot code
│── requirements.txt    # Python dependencies
│── README.md           # This file

🛠 Requirements

Python 3.9+

discord.py

openai

🔮 Future Ideas

/joke → AI jokes

/summarize → Summarize text or links

/translate → Translate messages into any language

Store conversation history per user
