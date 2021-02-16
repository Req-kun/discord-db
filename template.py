import main
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
#client = discord.Client(intents=discord.Intents.all())

TOKEN = ''


@bot.event
#@client.event
async def on_ready():
    await main.create_db(bot, 1234567890, 'dict')
    #await main.create_db(client, 1234567890, 'dict')

    bot.conn = await main.connect(bot, 1234567890, 0987654321)
    #client.conn = await main.connect(client, 1234567890, 0987654321)

    print(await bot.conn.content())
    #print(client.conn.content())

    await bot.conn.edit({'edited': 'content'})
    #client.conn.edit({'edited': 'content'})

    await bot.conn.remove_db()
    #client.conn.remove_db()


bot.run(TOKEN)
#client.run(TOKEN)
