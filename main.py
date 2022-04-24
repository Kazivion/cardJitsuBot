import discord
from discord.ext import commands
import asyncio
import random
import time

client = commands.Bot(command_prefix = '*', case_insensitive=True)

@client.event
async def on_ready():
    print('operation card jitsu is go'.format(client))

@client.command()
async def ping(ctx):
    await ctx.channel.send('Pong!')
    return

@client.command()
async def battle(ctx, opponent):

    # INVITE OPPONENT TO PLAY

    invitation = await ctx.channel.send('{}, {} has challenged you to card jitsu!\nOpponent must accept within 15 seconds or invitation is forfeit.'.format(opponent, ctx.message.author.mention))
    await invitation.add_reaction('✅')
    await invitation.add_reaction('❌')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["✅"] and reaction.message == invitation

    try:
        confirmation = await client.wait_for("reaction_add", check=check, timeout=15)

    except asyncio.TimeoutError:
        await ctx.channel.send('Ran out of time!')
        return

    if confirmation:
        await ctx.channel.send('Opponent accepted... starting game.')

    # COMMENCE GAMING

    def create_deck(n, player):
        # n = deck size
        cards = []
        for i in range(n):
            element = random.randint(0, 2)
            num = random.randint(2, 12)
            color = random.randint(0, 5)
            cards.append([element, num, color])

        print(cards)
        return cards

    #home_deck = player 1 guest_deck = player 2
    home_deck = create_deck(5, ctx.message.author)
    guest_deck = create_deck(5, opponent)

with open(r'C:\Users\Luke\Desktop\jitsu_token.txt') as f:
    client.run(f.read())
