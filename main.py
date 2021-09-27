import os
import discord

client = discord.Client()

#Bot starting event
@client.event
async def on_ready():
  print('We have logged in as user as {0.user}'.format(client))

#Specific Message recieving event
@client.event
async def on_message(message):
  #Assesing channel with specific ID to print
  ch = client.get_channel(891896869331013673)

  if message.author==client.user:
    #checking if message is sent by bot
    return
  
  if message.content.startswith('.'):
    await ch.send('@everyone\n New Chapter~ c{0} Released!'.format(message.content) 
    )#Replying to message

client.run(os.environ['bot'])
