import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.types import CallbackQuery
from google_trans_new import google_translator
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Get a bot token from botfather
TOKEN = os.environ.get("TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to your desired language__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("CHANNEL" ,url="https://t.me/TG_Free_Bots") ],
                 
           ]
        ) )
	
@app.on_message(filters.text & filters.private )
def echo(client, message):
 update_channel = "TG_Free_Bots"
 user_id = message.from_user.id
 if update_channel :
  try:
   client.get_chat_member(update_channel, user_id)
  except UserNotParticipant:
   message.reply_text("**__You are not subscribed my channel__** ",parse_mode="markdown", reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("Join our Bot's channel" ,url="https://t.me/TG_Free_Bots") ]
   ]))
   return
 
 keybord = InlineKeyboardMarkup( [
        [
            InlineKeyboardButton("Hindi", callback_data='hi'),
            InlineKeyboardButton("Kannada", callback_data='kn'),
            InlineKeyboardButton("malayalam",callback_data ='ml')
        ],
        [   InlineKeyboardButton("Tamil", callback_data='ta'),
        InlineKeyboardButton("Telugu", callback_data='te'),
        InlineKeyboardButton("English",callback_data = 'en')
        ],
        	[InlineKeyboardButton("Urdu",callback_data ="ur"),
	InlineKeyboardButton("Punjabi",callback_data="pa"),
	InlineKeyboardButton("Spanish",callback_data="es")
	]
    ]
 
 )

 
 message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup = keybord)
    
    
@app.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = google_translator()
  translated_text = translator.translate(tr_text,lang_tgt=cbdata)
  await update.message.edit(translated_text)
  	

app.run()
