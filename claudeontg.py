## ClaudeOnTG v0.2a
## by cosmicjoke1 
## github.com/cosmicjoke1/claudeonTG 
## GPL 3.0 license


## depends on Anthropic SDK and pyTelegramBotAPI
## there's another Python API for telegram as well, it's not that one
import telebot # type: ignore
from telebot import types # type: ignore
import anthropic # type: ignore
import os
from dotenv import load_dotenv

def envwrite(variable_name, value):
    with open('.env', 'a') as env_file:
        env_file.write(f'\n{variable_name}={value}')
envwrite("ANTH_API_KEY", input("Enter your Anthropic API key: "))
envwrite("TG_BOT_TOKEN", input("Enter your token from @BotFather: "))
#initialize environment variables
load_dotenv()
api_key = os.getenv('ANTH_API_KEY')
tgtoken = os.getenv('TG_BOT_TOKEN')



bot = telebot.TeleBot(tgtoken)
client = anthropic.Anthropic(api_key=api_key)

#context window to store conversation history
conversation_history = []
#token limit
MAX_TOKENS = 25000

#message handler
@bot.message_handler(func=lambda message: True) #listens for "did you send a message?" and reads it
def send_cmessage(message):
    #grabs the username from Telegram to inject it into the prompt - maintains user context
    username = str(message.from_user.username)
    conversation_history.append({"role": "user", "content": ("New message from " + username +" : "+ str(message.text))})

    #token limiter. removes old messages
    while sum(len(msg["content"].encode("utf-8")) for msg in conversation_history) > MAX_TOKENS:
        conversation_history.pop(0)

    response = client.messages.create(
        model="claude-3-opus-20240229",
        messages=conversation_history,
        max_tokens=2048,
    )
    conversation_history.append({"role": "assistant", "content": str(response.content[0].text)})
    #extract the text from the TextBlock
    msgtext = str(response.content[0].text)
    #escape char decode
    dcode_msg = bytes(msgtext, "utf-8").decode("unicode_escape")
    #send the message in Telegram
    bot.reply_to(message, dcode_msg)

bot.infinity_polling() #start polling, runs until halted. i am overcommenting this for the bit