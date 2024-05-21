## ClaudeOnTG v0.1a
## github.com/cosmicjoke1/claudeonTG
## GPL 3.0 license


#depends on Anthropic SDK and pyTelegramBotAPI
#there's another Python API for telegram as well, it's not that one

import telebot
from telebot import types
import anthropic


# Go to t.me/BotFather and use the command /newbot to generate the bot API token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

#bot bot telebot bot bot Bot teleBot
#this instantiates the actual bot object and links it to ur token (which also means the specific bot
#account on telegram.)
bot = telebot.TeleBot(BOT_TOKEN)

client = anthropic.Anthropic(
    api_key="YOUR_ANTHROPIC_API_KEY" #sorry dudes im not paying for ur Claude access im broke
)

#message handler
@bot.message_handler(func=lambda message: True) #listens for "did you send a message?" and reads it
def send_cmessage(message):
    #getting a little funky, i should probably rename these variables
    message1=[
        {"role": "user", "content": str(message.text)} #this message.text is from the TG bot api
    ]
    response = client.messages.create(
        #i formatted this whole thing weird. I'm tinkering with a system prompt.
        model="claude-3-opus-20240229",
        messages = message1,
        max_tokens = 1024,
    )
    
    #extract the text from the TextBlock
    msgtext = str(response.content[0].text)
    #escape char decode
    dcode_msg = bytes(msgtext, "utf-8").decode("unicode_escape")
    #send the message in Telegram
    bot.reply_to(message, dcode_msg)

bot.infinity_polling() #start polling, runs until halted. i am overcommenting this for the bit

