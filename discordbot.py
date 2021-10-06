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
   

code,name,weapon,attribute,affiliation,birthday,basishp,basisdefence,basisattack,criticalhit,critdamage,specificbonus
RI,雷電将軍,長柄,雷,稲妻城,6/26,1005→12907,61→789,26→337,5.0%,50.0%,0.0%→32.0%


@bot.command()
async def intro(ctx, *args):
   namepr = namelist.get(args[0])
   msg = introlist.get(namepr)
   
   embed=discord.Embed(color=0xff2e2e)
   embed.add_field(name=args[0], value=msg, inline=False)
   await ctx.send(embed=embed)
    

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)


