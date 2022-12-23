import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = ".", intents=intents)

@bot.event
async def on_ready():
    print('JD BOT LISTO')
    await bot.change_presence(activity=nextcord.Game('M03 OFIMÁTICA'), status=nextcord.Status.dnd)


@bot.command()
async def ping(ctx):
    await ctx.send(f'PONG! {round(bot.latency)}ms!')


bot.run('MTA1MzA1NTcwMjg1NzQzMzEyOQ.GoEWF0.i-MGPCEG4iQi3HsAtHU2U1CVGe84Rx0ogsKofc')