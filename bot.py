import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import discord
from discord.ext import commands
from time import sleep
from datetime import datetime
from colorama import Fore, Back, Style
from colorama import init
init()

bad_words = ['блять', 'блядь', 'сука', 'уебан', 'гондон', 'кондон', 'cука', 'тварь' ]
help_words = ['помощь', 'помогите', 'хелп', 'help']

PREFIX = '.'

client = commands.Bot(command_prefix='.')

data = str(datetime.today())


# auto default role
@client.event
async def on_member_join(member):
    role = discord.utils.get( member.guild.roles, id = 729325803501780994 )
    await member.add_roles( role )

# mute
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member:discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, id = 729325522928271431)
    await member.add_roles(mute_role)


#delete help
client.remove_command( 'help' )

# connect
@client.event
async def on_ready():
    print( Fore.GREEN + 'Бот успешно подключён !!!')

    await client.change_presence( status = discord.Status.online, activity = discord.Game('Пажылова таракана') )

# unban
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    baned_users = await ctx.guild.bans()

    for ban_entre in baned_users:
        user = ban_entre.user

        await ctx.guild.unban(user)

        await ctx.send(f' {user.mention} теперь снова с нами !')

        sleep(5)
        await ctx.channel.purge(limit=1)

        return

        print(Fore.GREEN + 'Разбанили Userа ' + data)




# ban
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    sleep(2)
    await ctx.send(f'User {member.mention} был забанен')
    sleep(10)
    await ctx.channel.purge(limit=1)

    print(Fore.RED + 'Забанили Userа ' + data)


# list ban
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def banlist( ctx ):
	await ctx.channel.purge(limit=1)
	baned_users = await ctx.guild.bans()
	await ctx.send(baned_users)

# kick
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f'User {member.mention} был кикнут')
    sleep(10)
    await ctx.channel.purge(limit=1)
    print(Fore.RED + 'Кикнули Userа ' + data)


# clear
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def cc(ctx, amount=100):
	await ctx.channel.purge(limit=int(amount))
	emb = discord.Embed( colour=discord.Color.green())
	emb.add_field(name='Успешно', value = 'Отчищенно')
	await ctx.send(embed=emb)
	sleep(1)
	await ctx.channel.purge(limit=1)

#helper
# command
# bad_words
@client.event
async def on_message(message):
    await client.process_commands(message)

    msg = message.content.lower()

    if msg in bad_words:
        await message.delete()
        sleep(1)
        await message.author.send(f' Такое не надо писать')

        print(Fore.YELLOW + 'Спам ' + data)

    if msg in help_words:
        await message.delete()
        sleep(1)
        embed = discord.Embed(title="Discord.py | python bot", color=0x00ffff)
        embed.add_field(name="Для помощи по серверу введите коомманду", value=".help", inline=True)
        embed.set_footer(text="С уважением Discord.py | python bot")
        await message.author.send(embed = embed)

#command help
@client.command( pass_context = True)
async def help( ctx ):
	await ctx.channel.purge(limit=1)
	emb = discord.Embed(title = 'Помощь по серверу ', colour = discord.Color.blue())

	emb.add_field(name = '{}cc'.format( PREFIX ), value = 'Отчистка чата')
	emb.add_field(name= '{}kick'.format(PREFIX), value='Кик')
	emb.add_field(name= '{}ban'.format(PREFIX), value='Бан')
	emb.add_field(name= '{}unban'.format(PREFIX), value='Разбан')
	emb.set_image(url = 'https://wiki.awin.com/images/3/3d/Help.jpg')


	await ctx.author.send( embed = emb )


# connect
# token = 'NzI4OTg4NDYxOTg5NzU2OTk4.XwDPeg.p5M7kEnCnUfOJIrLBL-Nn3lcdR0'

token = os.environ.get('BOT_TOKEN')


bot.run(str(token))



