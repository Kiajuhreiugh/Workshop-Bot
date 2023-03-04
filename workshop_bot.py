import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/wsb ')

@client.event
async def on_ready():
    print('Workshop Bot is ready.')

@client.command()
async def setgithub(ctx, github):
    # Save the github link for this user
    pass

@client.command()
async def post(ctx, title, code, notes):
    if ctx.channel.name != 'workshop':
        return

    # Get the github link for this user
    github_link = ''

    # Format the response message
    response = f'{ctx.author} posted {title}\nCode: {code}\nGithub: {github_link}\n{notes}'

    # Send the response to the "#workshop" channel
    await ctx.send(response)

# Replace 'YOUR_BOT_TOKEN' with your bot's token
client.run('YOUR_BOT_TOKEN')
