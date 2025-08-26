import discord
from discord import app_commands
import openai

DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

openai.api_key = OPENAI_API_KEY

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync commands with Discord
        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# ---- SLASH COMMAND ----
@bot.tree.command(name="ask", description="Ask AI a question")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()  # Acknowledge command (prevents timeout)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    answer = response["choices"][0]["message"]["content"]

    await interaction.followup.send(answer)

bot.run(DISCORD_TOKEN)
