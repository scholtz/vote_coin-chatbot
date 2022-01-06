import discord #import all the necessary modules
import os
import nltk
from neuralintents import GenericAssistant


nltk.download('omw-1.4')


chatbot = GenericAssistant('intents2.json')
chatbot.train_model()
chatbot.save_model()

print('bot done training')


client = discord.Client()

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

        
    if message.content.startswith('Bot'):
        response = chatbot.request(message.content[4:])
        await message.channel.send(response)

print('running bot with token')
print(os.environ['token'])

client.run(os.environ['token'])


print('finished')

