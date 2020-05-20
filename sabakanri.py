import discord
import sys

TOKEN = '#####################################################'
update_date = "2020/05/20"
author = "Wamo"
version = "1.5"
client = discord.Client()

@client.event
async def on_ready():
    print("ログインしました")
    await client.change_presence(activity=discord.Game(name='通常稼働中'))

@client.event
async def on_guild_update(before, after):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下の要素が変更されました",description='更新前：\n' + str(before) + '\n\n更新後：\n' + str(after),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_guild_role_create(role):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下のロールが作成されました",description='ロール：\n' + str(role),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_guild_role_delete(role):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下のロールが削除されました",description='ロール：\n' + str(role),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_member_ban(guild, user):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下のユーザーがBANされました",description='ユーザー：\n' + str(user),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_member_unban(guild, user):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下のユーザーのBANが解除されました",description='ユーザー：\n' + str(user),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_guild_role_update(before, after):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下のロールが更新されました",description='ロール：\n' + str(after),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_guild_channel_delete(channel):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下のチャンネルが削除されました",description='チャンネル：\n' + str(channel),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_guild_channel_create(channel):
    CHANNEL_ID = ##################
    channel = client.get_channel(CHANNEL_ID)
    embed = discord.Embed(title="以下のチャンネルが作成されました",description='チャンネル：\n' + str(channel),color=0x0076ff)
    embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
    await channel.send(embed = embed)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == ':help':
        embed = discord.Embed(title="使い方",color=0x0076ff)
        embed.add_field(name=":help",value="このページ",inline=False)
        embed.add_field(name=":about",value="このプログラムについて",inline=False)
        embed.add_field(name=":exit",value="終了",inline=False)
        embed.add_field(name="その他",value="サーバーの更新があった場合自動で通知します。",inline=False)
        embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
        await message.channel.send(embed = embed)

    if message.content == ':about':
        embed = discord.Embed(title="このBotについて",description='このBotは、サーバーに更新があったときに自動で通知するBotです。\n\n製作者：' + author + '\nバージョン：v' + version + '\n最終更新日：' + str(update_date),color=0x0076ff)
        embed.set_thumbnail(url="https://dl.accessto.net/image/40px-info.png")
        await message.channel.send(embed = embed)

    if message.content == ':exit':
        await client.logout()
        await sys.exit()

client.run(TOKEN)
