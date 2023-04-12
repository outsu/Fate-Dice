import discord
import random
import time

from discord import default_permissions
from discord.ext import commands


intents = discord.Intents.default()
client = discord.Bot(command_prefix='F', help_command=None,intents=intents)
token = "TOKEN_HERE"

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(str(len(client.guilds)) + ' server.'))
    try:
        synced = await client.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)
    print('Ready.')

@client.command(description="roll")
async def roll(ctx, a: int = None):
    zarList = [1, -1, 0]

    zarsonuc = random.choices(zarList, k=4)

    if a:
        zarsonucsayi = sum(zarsonuc, a)
    else:
        zarsonucsayi = sum(zarsonuc)

    if zarsonucsayi == 0:
        dic = {1: '<:mavi_arti:749335608849072159>', -1: '<:mavi_eksi:749335609155387392>',
               0: '<:mavi_bos:749335608949866657>'}
    elif zarsonucsayi > 0:
        dic = {1: '<:yesil_arti:749340146868158476>', -1: '<:yesil_eksi:749340147325075557>',
               0: '<:yesil_bos:749340147342114836>'}
    elif zarsonucsayi < 0:
        dic = {1: '<:kirmizi_arti:749340106812424323>', -1: '<:kirmizi_eksi:749340107122671687>',
               0: '<:kirmizi_bos:749340109593378906>'}

    sonuc = [dic.get(n, n) for n in zarsonuc]

    zardebug = [zarsonucsayi, '']

    # zrsnsy = f"{zarsonucsayi}"
    if -4 <= zarsonucsayi <= 8:
        zartanim = {-4: 'Abysmal', -3: 'Bad', -2: 'Terrible', -1: 'Poor', 0: 'Mediocre', 1: 'Average', 2: 'Fair',
                    3: 'Good', 4: 'Great', 5: 'Superb', 6: 'Fantastic', 7: 'Epic', 8: 'Legendary'}
        tanimsonuc = [zartanim.get(n, n) for n in zardebug]
        wth = " ".join(map(str, tanimsonuc))
    else:
        wth = "**Extraordinary?!**"
    wth2 = " ".join(map(str, sonuc))

    if not a:
        await ctx.respond(ctx.user.mention + f" rolls {wth}({sum(zarsonuc)}) dice.{wth2}")
    elif a >= 0:
        await ctx.response.send_message(ctx.user.mention + f" rolls {wth}({sum(zarsonuc)}*+{a}*) dice.{wth2}")
    elif a < 0:
        await ctx.response.send_message(ctx.user.mention + f" rolls {wth}({sum(zarsonuc)}*{a}*) dice.{wth2}")


@client.command(name="dmroll")
async def dmroll(ctx:discord.Interaction, a: int = None):
    zarList = [1, -1, 0]

    zarsonuc = random.choices(zarList, k=4)

    if a:
        zarsonucsayi = sum(zarsonuc, a)
    else:
        zarsonucsayi = sum(zarsonuc)

    if zarsonucsayi == 0:
        dic = {1: '<:mavi_arti:749335608849072159>', -1: '<:mavi_eksi:749335609155387392>',
               0: '<:mavi_bos:749335608949866657>'}
    elif zarsonucsayi > 0:
        dic = {1: '<:yesil_arti:749340146868158476>', -1: '<:yesil_eksi:749340147325075557>',
               0: '<:yesil_bos:749340147342114836>'}
    elif zarsonucsayi < 0:
        dic = {1: '<:kirmizi_arti:749340106812424323>', -1: '<:kirmizi_eksi:749340107122671687>',
               0: '<:kirmizi_bos:749340109593378906>'}

    sonuc = [dic.get(n, n) for n in zarsonuc]

    zardebug = [zarsonucsayi, '']

    # zrsnsy = f"{zarsonucsayi}"
    if -4 <= zarsonucsayi <= 8:
        zartanim = {-4: 'Abysmal', -3: 'Bad', -2: 'Terrible', -1: 'Poor', 0: 'Mediocre', 1: 'Average', 2: 'Fair',
                    3: 'Good', 4: 'Great', 5: 'Superb', 6: 'Fantastic', 7: 'Epic', 8: 'Legendary'}
        tanimsonuc = [zartanim.get(n, n) for n in zardebug]
        wth = " ".join(map(str, tanimsonuc))
    else:
        wth = "**Extraordinary?!**"
    wth2 = " ".join(map(str, sonuc))

    atici = ctx.user
    if not a:
        await atici.send(f"You roll {wth}({sum(zarsonuc)}) dice.{wth2}")
        await ctx.response.send_message("DM'd!", ephemeral=True)
    elif a >= 0:
        await atici.send(f"You roll {wth}({sum(zarsonuc)}*+{a}*) dice.{wth2}")
        await ctx.response.send_message("DM'd!", ephemeral=True)
    elif a < 0:
        await atici.send(f"You roll {wth}({sum(zarsonuc)}*{a}*) dice.{wth2}")
        await ctx.response.send_message("DM'd!", ephemeral=True)


@client.command()
async def refreshserver(ctx):
    swsay = str(len(client.guilds))
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(str(len(client.guilds)) + 'server.'))
    await ctx.response.send_message(f"Refreshed: {swsay}")


@client.command(name="help", description="Help for bot commands, /help report *your text* to DM ayran about bot.")
async def help(ctx:discord.Interaction):
    embed = discord.Embed(title="Commands", color=0xff0000)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/744942350757003385/90038456c833a0588eda7722c88293f3.webp")
    embed.add_field(name="**/**roll (skill point)", value="Roll in text channel.", inline=False)
    embed.add_field(name="**/**dmroll (skill point)", value="Send your roll result to DM.", inline=False)
    embed.add_field(name="**/**report ", value="DM bot dev via bot, <@323185438959468546>.", inline=False)
    embed.set_footer(text=f"Dev: 323185438959468546, ayran#4627")
    await ctx.response.send_message(embed=embed)

@client.command(name="report", describtion="Report bugs or ask questions to developer of the bot, ayran#4627")
async def help(ctx:discord.Interaction, text:discord.Option(str, "Enter your report",default='')):

    owner = await client.fetch_user("323185438959468546")
    embed = discord.Embed(title=f"New Report from {ctx.user.name}!", color=0xff0000)
    embed.set_thumbnail(url=ctx.user.avatar)
    embed.add_field(name="Report:",value=text)
    embed.add_field(name="",value=ctx.user.mention,inline=False)
    embed.set_footer(text=f"{ctx.guild_id}")
    await owner.send(embed=embed)
    await ctx.response.send_message("Report sent to owner, <@323185438959468546>", ephemeral=True)

client.run(token)
