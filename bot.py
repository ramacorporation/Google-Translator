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


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TOKEN","1721526338:AAEqf3-MMZN7jZworK5q2dxUNQJgKPqWva8")
APP_ID =int(os.environ.get("APP_ID",2383784))
API_HASH =os.environ.get("API_HASH","b45d5731ba5e5b15e38fcee3386c50c7")
app = Client(
        "ggt",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
    )
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("CHANNEL" ,url="https://t.me/TG_Free_Bots") ],
                  
           ]
        ) )

	
@app.on_message(filters.text & filters.private )
def echo(client, message):
 
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
