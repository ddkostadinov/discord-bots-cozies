import os
from re import T
import discord
import datetime
import time
import random
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True

my_secret = '[insert secret]' #change after test
client = discord.Client(intents=intents)



time_now = datetime.datetime.now
t = datetime.time

copies = ["The Diamond Ticket. Trade, reveal or keep it - it's your choice. WL Mint: **2 Nov, 2022 / 10am EST (24 hours).** Public Mint: **3Nov, 2022 /10am EST (24 hours).** \n\nMore about the mint method here: <#1026854780934565958>"]

diamond_copies = ["<@&1031593747353436170> remember to submit your Metamask Ethereum address to <#1031596602940456960>\n\nIf you’d like to level up to get more 💎, do check out <#1026854780934565958>"]


dts = [t(1), t(3), t(5), t(7), t(9), t(11), t(13), t(15), t(17), t(19), t(21), t(23)]
diamond_dts = [t(2), t(4), t(6), t(8), t(10), t(12), t(14), t(16), t(18), t(20), t(22)]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  myLoop.start()
 
  
@tasks.loop(time = dts)
async def myLoop():
  channel = client.get_channel('[channel-id]')  # change after test
  await channel.send(random.choice(copies), file=discord.File('./theDiamondTicket.mov'))
  time.sleep(2)
  
@tasks.loop(time = diamond_dts)
async def myDiamondLoop():
  channel = client.get_channel('[channel-id]')  # change after test
  await channel.send(diamond_copies[0])
  time.sleep(2)
  
  
  
  
  
  
  

  
client.run(my_secret)
