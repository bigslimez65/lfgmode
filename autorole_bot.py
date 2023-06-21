import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

role_a = None
role_b = None
is_role_switched = False


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_member_join(member):
    global role_a, role_b, is_role_switched
    role = role_b if is_role_switched else role_a
    await member.add_roles(role)
    system_channel = member.guild.system_channel
    if system_channel is not None:
        await system_channel.send(f"Welcome, {member.mention}! The currently selected role for new members is {role.name}.")
    print(f"New member joined: {member.name}")
    print(f"Assigned role: {role.name}")


@bot.command()
async def swaprole(ctx):
    global role_a, role_b, is_role_switched
    if not role_a or not role_b:
        await ctx.send("Roles have not been set.")
        return

    is_role_switched = not is_role_switched
    role = role_b if is_role_switched else role_a
    await ctx.send(f"The currently selected role for new members is now {role.name}.")


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_connect():
    global role_a, role_b
    guild = await bot.fetch_guild(1106325655232184433)
    role_a = discord.utils.get(guild.roles, name='Homie')
    role_b = discord.utils.get(guild.roles, name='LFG')


bot.run('MTEyMDc2ODkwNDcyMjEyODkyNg.GAcgIw.FoCL0fbKK9Ea8kNXFrY5YVjs2SDOqZLL8_fBqA')
