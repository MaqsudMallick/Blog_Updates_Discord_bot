import os
#For Discord
import discord
client = discord.Client()
#For Selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(options=chrome_options)
from keep_alive import keep_alive

# driver.get("https://shiny-made.github.io/bs")

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
    await ch.send('@everyone \n New Chapter~ Released!\nLink: https://shiny-made.github.io/bswehcf-c{0}         \nAdvanced Chapter: https://www.patreon.com/shinyMade'.format(message.content[1:2]) 
    )#Replying to message

keep_alive()
client.run(os.environ['bot'])
