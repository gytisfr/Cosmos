#Cosmos by Gytis


#Imports
import discord.utils
import youtube_dl
import discord
import asyncio
import random
import os
import re
from discord_buttons import DiscordButton, Button, ButtonStyle, InteractionType
from discord.ext import commands
from discord.utils import get
from discord.ext import menus
os.chdir("D:\Bot Clients\Cosmos")


#Vars
client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())
client.remove_command('help')
ddb = DiscordButton(client)


#Def
def botdev(ctx):
    return ctx.author.id in [301014178703998987]
    #Me


#Events
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!help"))
    print('Cosmos now online!')

@client.event
async def on_message(message):
    def check(m):
        return m.author == message.author
    if message.content.startswith('!giveaway'):
        channel1 = message.channel
        await channel1.send('Title of the embed')
        
        msg1 = await client.wait_for('message', check=check)
        await channel1.send("Description of the embed")

        msg2 = await client.wait_for('message', check=check)
        await channel1.send("Emoji you want the reaction to be")

        msg3 = await client.wait_for('message', check=check)
        await channel1.send("Mention the channel you want the giveaway sent to")

        msg4 = await client.wait_for('message', check=check)
        embed = discord.Embed(
            title=msg1.content,
            colour=0x000000,
            description=msg2.content
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        chanid1 = re.split("<#", str(msg4.content))
        chanid2 = re.split(">", str(chanid1[1]))
        chanidfin = str(chanid2[0])
        chanfin = client.get_channel(int(chanidfin))
        msgfinal = await chanfin.send(embed=embed)
        await msgfinal.add_reaction(msg3)
    else:
        pass
    if message.content.startswith('<@885941977252757505>' or '<@!885941977252757505>'):
        await message.channel.send("My prefix is !")
    else:
        pass
    await client.process_commands(message)


#Commands
#Moderation
#Clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    channel = discord.utils.get(ctx.guild.text_channels, name='logs')
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title = 'Clear',
        colour = 0x000000,
        description = f'{ctx.author.mention} has cleared {amount} messages'
    )
    embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
    msg = await ctx.send(embed=embed)
    embed = discord.Embed(
        title = 'Clear',
        colour = 0x000000,
        description = f'{ctx.author.mention} has cleared {amount} messages in {ctx.channel.mention}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
    await channel.send(embed=embed)
    await asyncio.sleep(3)
    await msg.delete()

#Warn
@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    channel = discord.utils.get(ctx.guild.text_channels, name='logs')
    await ctx.message.delete()
    if reason:
        embed = discord.Embed(
            title="Warn",
            colour=0x000000,
            description=f"{ctx.author.mention} has warned {member.mention} for:\n{reason}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        msg = await ctx.send(embed=embed)
        await channel.send(embed=embed)
        embed = discord.Embed(
            title="Warn",
            colour=0x000000,
            description=f"{ctx.author.mention} has warned you for:\n{reason}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        memberdm = await member.create_dm()
        await memberdm.send(embed=embed)
        await asyncio.sleep(3)
        await msg.delete()
    else:
        embed = discord.Embed(
            title="Warn",
            colour=0x000000,
            description=f"{ctx.author.mention} has warned {member.mention}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        msg = await ctx.send(embed=embed)
        await channel.send(embed=embed)
        embed = discord.Embed(
            title="Warn",
            colour=0x000000,
            description=f"{ctx.author.mention} has warned you"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        memberdm = await member.create_dm()
        await memberdm.send(embed=embed)
        await asyncio.sleep(3)
        await msg.delete()

#Kick
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    channel = discord.utils.get(ctx.guild.text_channels, name='logs')
    await ctx.message.delete()
    if reason:
        embed = discord.Embed(
            title="Kick",
            colour=0x000000,
            description=f"{ctx.author.mention} has kicked {member.mention} for:\n{reason}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        msg = await ctx.send(embed=embed)
        await channel.send(embed=embed)
        embed = discord.Embed(
            title="Kick",
            colour=0x000000,
            description=f"{ctx.author.mention} has kicked you for:\n{reason}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        memberdm = await member.create_dm()
        await memberdm.send(embed=embed)
        await member.kick()
        await asyncio.sleep(3)
        await msg.delete()
    else:
        embed = discord.Embed(
            title="Kick",
            colour=0x000000,
            description=f"{ctx.author.mention} has kicked {member.mention}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        msg = await ctx.send(embed=embed)
        await channel.send(embed=embed)
        embed = discord.Embed(
            title="Kick",
            colour=0x000000,
            description=f"{ctx.author.mention} has kicked you"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        memberdm = await member.create_dm()
        await memberdm.send(embed=embed)
        await member.kick()
        await asyncio.sleep(3)
        await msg.delete()

#Ban
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    channel = discord.utils.get(ctx.guild.text_channels, name='logs')
    await ctx.message.delete()
    if reason:
        embed = discord.Embed(
            title="Ban",
            colour=0x000000,
            description=f"{ctx.author.mention} has banned {member.mention} for {reason}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        msg = await ctx.send(embed=embed)
        await channel.send(embed=embed)
        embed = discord.Embed(
            title="Ban",
            colour=0x000000,
            description=f"{ctx.author.mention} has banned you for:\n{reason}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        memberdm = await member.create_dm()
        await memberdm.send(embed=embed)
        await member.ban()
        await asyncio.sleep(3)
        await msg.delete()
    else:
        embed = discord.Embed(
            title="Ban",
            colour=0x000000,
            description=f"{ctx.author.mention} has banned {member.mention}"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        msg = await ctx.send(embed=embed)
        await channel.send(embed=embed)
        embed = discord.Embed(
            title="Ban",
            colour=0x000000,
            description=f"{ctx.author.mention} has banned you"
        )
        embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
        memberdm = await member.create_dm()
        await memberdm.send(embed=embed)
        await member.ban()
        await asyncio.sleep(3)
        await msg.delete()



#Giveaway End
@client.command()
async def end(ctx, *, message : discord.Message):
    users = await message.reactions[0].users().flatten()
    users = [member for member in users if member.id != client.user.id]
    winner = random.choice(users)
    embed = discord.Embed(
        title="Giveaway",
        colour=0x000000,
        description=f"The winner is; {winner.mention}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/bKpryHy/photo-1518066000714-58c45f1a2c0a.jpg")
    await ctx.send(embed=embed)



#Fun
#Fun
@client.command()
async def fun(ctx):
    await ctx.send("Is this bot fun yet")



#Run Token
client.run('ODg1OTQxOTc3MjUyNzU3NTA1.YTuXww.51aDiPFX8KoFJR-QbcCuYSqFP20')