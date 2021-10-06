from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

data = [
    ['2019-07-01 15:00:00','9997','740'],
    ['2019-07-02 15:00:00','9997','749'],
    ['2019-07-03 15:00:00','9997','757'],
    ['2019-07-04 15:00:00','9997','769'],
    ['2019-07-05 15:00:00','9997','762'],
    ['2019-07-08 15:00:00','9997','760']
]


df = pd.DataFrame(data)
print(df)
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)


