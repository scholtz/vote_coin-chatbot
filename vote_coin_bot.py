import discord #import all the necessary modules
import os
import sys
from slugify import slugify
from neuralintents import BasicAssistant
import contextlib
import requests

print('bot is starting')

chatbot = BasicAssistant('intents2.json')
chatbot.fit_model(epochs=50)


def price_usdc_vote():
    url = ' https://api.vote-coin.com/Price/Get/452399768/31566704'
    json = requests.get(url).json()
    price = json
    return price

def price_algo_vote():
    url = 'https://api.vote-coin.com/Price/Get/452399768/0'
    json = requests.get(url).json()
    price = json
    return price

def price_vote_usdc():
    url = ' https://api.vote-coin.com/Price/Get/31566704/452399768'
    json = requests.get(url).json()
    price = json
    return price

def price_vote_algo():
    url = 'https://api.vote-coin.com/Price/Get/0/452399768'
    json = requests.get(url).json()
    price = json
    return price

print('bot done training')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    text = slugify(message.content)

    print("Request received")
    print(text)
    print(message.content.strip())
    
    if text.startswith('bot-'):
        if text == 'bot' and message.content.strip().endswith(' $'):
            price = price_usdc_vote()
            await message.channel.send("The current price is " + str(price) + " USDC/$vote")
        elif text == 'bot-usdc':
            price = price_usdc_vote()
            await message.channel.send("The current price is " + str(price) + " USDC/$vote")
        elif text == 'bot-algo':
            price = price_algo_vote()
            await message.channel.send("The current price is " + str(price) + " ALGO/$vote")
        elif text == 'bot-voteusdc':
            price = price_vote_usdc()
            await message.channel.send("The current price is " + str(price) + " $vote/USDC")
        elif text == 'bot-votealgo':
            price = price_vote_algo()
            await message.channel.send("The current price is " + str(price) + " $vote/ALGO")
        elif text == 'bot-usdcvote':
            price = price_usdc_vote()
            await message.channel.send("The current price is " + str(price) + " USDC/$vote")
        elif text == 'bot-algovote':
            price = price_algo_vote()
            await message.channel.send("The current price is " + str(price) + " ALGO/$vote")
        elif text == 'bot' and message.content.strip().endswith('?'):
            await message.channel.send("Current commands: 'Bot VOTEUSDC|VOTEALGO|USDCVOTE|ALGOVOTE'")
        elif text == 'bot-help':
            await message.channel.send("Current commands: 'Bot VOTEUSDC|VOTEALGO|USDCVOTE|ALGOVOTE'")
        else:
            response = chatbot.process_input(message.content[4:])
            await message.channel.send(response)

print('running bot with token')
print(os.environ['token'])

client.run(os.environ['token'])


print('finished')

