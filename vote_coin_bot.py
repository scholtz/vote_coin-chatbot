import discord #import all the necessary modules
import os
import nltk
from neuralintents import GenericAssistant


nltk.download('omw-1.4')


chatbot = GenericAssistant('intents2.json')
chatbot.train_model()
chatbot.save_model()


def price_usdc_vote():
    url = ' https://api.vote-coin.com/Price/Get/31566704/452399768'
    json = requests.get(url).json()
    price = json
    return price

def price_algo_vote():
    url = 'https://api.vote-coin.com/Price/Get/0/452399768'
    json = requests.get(url).json()
    price = json
    return price

def price_vote_usdc():
    url = ' https://api.vote-coin.com/Price/Get/452399768/31566704'
    json = requests.get(url).json()
    price = json
    return price

def price_vote_algo():
    url = 'https://api.vote-coin.com/Price/Get/452399768/0'
    json = requests.get(url).json()
    price = json
    return price

print('bot done training')
client = discord.Client()

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

        
    if message.content.startswith('Bot'):
        if message.content == 'Bot $'
            price = price_usdc_vote()
            await message.channel.send("The current price USDC/$vote is " + str(price))
        elif message.content == 'Bot USDC'
            price = price_usdc_vote()
            await message.channel.send("The current price USDC/$vote is " + str(price))
        elif message.content == 'Bot ALGO'
            price = price_algo_vote()
            await message.channel.send("The current price ALGO/$vote is " + str(price))
        elif message.content == 'Bot VOTEUSDC'
            price = price_vote_usdc()
            await message.channel.send("The current price $vote/USDC is " + str(price))
        elif message.content == 'Bot VOTEALGO'
            price = price_vote_algo()
            await message.channel.send("The current price $vote/ALGO is " + str(price))
        elif message.content == 'Bot USDCVOTE'
            price = price_usdc_vote()
            await message.channel.send("The current price USDC/$vote is " + str(price))
        elif message.content == 'Bot ALGOVOTE'
            price = price_algo_vote()
            await message.channel.send("The current price ALGO/$vote is " + str(price))
        elif message.content == 'Bot ?'
            await message.channel.send("Current commands: 'Bot VOTEUSDC|VOTEALGO|USDCVOTE|ALGOVOTE' " + str(price))
        else
            response = chatbot.request(message.content[4:])
            await message.channel.send(response)

print('running bot with token')
print(os.environ['token'])

client.run(os.environ['token'])


print('finished')

