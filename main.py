import os
import discord
import openai
from discord.ext import commands

openai.api_key = os.getenv("OPENAI_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} جاهز!")

@bot.command()
async def raven(ctx, *, question):
    prompt = f"""
    أنتِ شخصية أنثوية تُدعى رايفن، تتحدثين بالعربية، وتردين بأسلوب فلسفي، غامض، وذكي.
    السؤال: {question}
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.8
    )
    await ctx.send(response.choices[0].text.strip())

bot.run(DISCORD_TOKEN)
