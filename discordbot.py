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
    
    
code,name,health,fastest_ground,ra_ground,clash_assault,overhead,overhead_frame,commandgrab,commandgrab_frame,antiair,antiair_frame,antiair_inv,role
RG,ラグナ,17000,4A-5F,10,22,214B,18(前方への判定発生は22),ー,ー,5B,11,4~11,Point
JI,ジン,17000,4A-6F,13,22,J214C,23,ー,ー,2B,14,8~16,Support
NO,ノエル,17000,2A-7F,10,22,ー,ー,214A,29(立ち状態のみ),4A,8,6~8,Point
RA,レイチェル,17000,5A-8F,16,22,JA,13,ー,ー,4A,13,5~12(ガードポイント),Flex
TG,テイガー,20000,214A.214C-6F,16,22,ー,ー,214A.214C,6,2B,13,9~12,Support
HK,ハクメン,18000,2A-8F,1,22,J214C,20,ー,ー,2B,13,9~15,Point
NU,ニュー,16000,5A-9F,20,22,JC,21,ー,ー,4A,11,5~11,Point
HZ,ハザマ,17000,236BC-5F,10,22,236B,30,214C,15,2B,13,8~15,Point
MK,マコト,17000,4A-5F,9,26,ー,ー,ー,ー,5B,11,5~14,Point
PL,プラチナ,17000,4A-6F,11,22,JC,19,ー,ー,5B,12,6~15,Point
IZ,イザヨイ,17000,4A-6F,14,22,66>JA,19,ー,ー,214B,10,4~12,Point
AZ,アズラエル,18000,4A-6F,18,26,236C,24,ー,ー,2B,13,7~16,Point


@bot.command()
async def intro(ctx, *args):
   if len(args) == 0:
       await ctx.send('引数にキャラクターの名前を入力してください。')
       return
   namepr = namelist.get(args[0])
   if namepr == None:
       await ctx.send('存在しないキャラクター、またはキャラクターの名前が間違っています。')
       return
   msg = introlist.get(namepr)
   
   embed=discord.Embed(color=0xff2e2e)
   embed.add_field(name=args[0], value=msg, inline=False)
   embed.set_footer(text="引用元：BBTAG Character Overview")
   await ctx.send(embed=embed)


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)


