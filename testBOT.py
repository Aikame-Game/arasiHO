import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print('ログインしました')


@client.command()
async def RC(ctx):
    await ctx.send('<@1096388219483987978>ユーザー名を入力してください。それで、報告完了です。')


client.run('MTIxMzc3NzAwNTQ4NTYyMTI3OA.GgUKEa.lEJLlaydc87IZ86-Ml2k9FwYqv3MtGXcJ-V8sk')