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

PREVIOUS_TEXT = """hi"""
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to your desired language__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("CHANNEL" ,url="https://t.me/TG_Free_Bots") ],
                [   InlineKeyboardButton("All our FREE BOTS" ,url="https://t.me/TG_Free_Bots/3")]
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
   message.reply_text("**__Join our Bot's Channel to use ME__** ",parse_mode="markdown", reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("Join our Bot's channel" ,url="https://t.me/TG_Free_Bots") ]
   ]))
   return
 
 keybord = InlineKeyboardMarkup( [
       
            [   InlineKeyboardButton("Afrikaans", callback_data='af'),
        InlineKeyboardButton("Albanian", callback_data='sq'),
        InlineKeyboardButton("Amharic",callback_data = 'am'),
        InlineKeyboardButton("Arabic", callback_data='ar'),
	],
	[   InlineKeyboardButton("Armenian", callback_data='hy'),
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),
        InlineKeyboardButton("Basque", callback_data='eu')
	],
	[   InlineKeyboardButton("Belarusian", callback_data='be'),
        InlineKeyboardButton("Bengali",callback_data = 'bn'),
        InlineKeyboardButton("Bosnian", callback_data='bs')
	],
        [    InlineKeyboardButton("Bulgarian", callback_data='bg'),
        InlineKeyboardButton("Catalan",callback_data = 'ca'),
        InlineKeyboardButton("Cebuano", callback_data='ceb'),
        InlineKeyboardButton("Chichewa", callback_data='ny')
	],
        [   InlineKeyboardButton("Chinese (simplified)",callback_data = 'zh-cn'),
        InlineKeyboardButton("Chinese (traditional)", callback_data='zh-tw')
	],
        [   InlineKeyboardButton("Corsican", callback_data='co'),
        InlineKeyboardButton("Croatian",callback_data = 'hr'),
        InlineKeyboardButton("Czech", callback_data='cs'),
        InlineKeyboardButton("Danish", callback_data='da')
	 ],
        [   InlineKeyboardButton("Dutch",callback_data = 'nl'),
        InlineKeyboardButton("English", callback_data='en'),
        InlineKeyboardButton("Esperanto", callback_data='eo'),
        InlineKeyboardButton("Estonian",callback_data = 'et')
        ],
        [   InlineKeyboardButton("Filipino", callback_data='tl'),
        InlineKeyboardButton("Finnish", callback_data='fi'),
        InlineKeyboardButton("French",callback_data = 'fr'),
        InlineKeyboardButton("Frisian", callback_data='fy')
	 ],
        [   InlineKeyboardButton("Galician", callback_data='gl'),
        InlineKeyboardButton("Georgian",callback_data = 'ka'),
        InlineKeyboardButton("German", callback_data='de'),
        InlineKeyboardButton("Greek", callback_data='el')
	 ],
        [   InlineKeyboardButton("Gujarati",callback_data = 'gu'),
        InlineKeyboardButton("Haitian Creole", callback_data='ht'),
        InlineKeyboardButton("Hausa", callback_data='ha')
	 ],
        [InlineKeyboardButton("Hawaiian",callback_data = 'haw'),
        InlineKeyboardButton("Hebrew", callback_data='iw'),
        InlineKeyboardButton("Hindi", callback_data='hi'),
        InlineKeyboardButton("Hmong",callback_data = 'hmn')
        ],
          [   InlineKeyboardButton("Hungarian", callback_data='hu'),
        InlineKeyboardButton("Icelandic", callback_data='is'),
        InlineKeyboardButton("Igbo",callback_data = 'ig')
	   ],
        [   InlineKeyboardButton("Indonesian", callback_data='id'),
	InlineKeyboardButton("Irish", callback_data='ga'),
        InlineKeyboardButton("Italian",callback_data = 'it')
	 ],
        [   InlineKeyboardButton("Japanese", callback_data='ja'),
	InlineKeyboardButton("Javanese", callback_data='jv'),
	InlineKeyboardButton("Kannada",callback_data = 'kn'),
        InlineKeyboardButton("Kazakh", callback_data='kk')
	 ],
        [   InlineKeyboardButton("Khmer", callback_data='km'),
        InlineKeyboardButton("Kinyarwanda", callback_data='rw'),
        InlineKeyboardButton("Korean",callback_data = 'ko')
        ],
          [   InlineKeyboardButton("Kurdish", callback_data='ku'),
        InlineKeyboardButton("Kyrgyz", callback_data='ky'),
        InlineKeyboardButton("Lao",callback_data = 'lo'),
        InlineKeyboardButton("Latin", callback_data='la')
	   ],
        [InlineKeyboardButton("Latvian", callback_data='lv'),
        InlineKeyboardButton("Lithuanian",callback_data = 'lt')
        ],
          [   InlineKeyboardButton("Luxembourgish", callback_data='lb'),
        InlineKeyboardButton("Macedonian", callback_data='mk')
	   ],
        [   InlineKeyboardButton("Malagasy",callback_data = 'mg'),
        InlineKeyboardButton("Malay", callback_data='ms'),
	InlineKeyboardButton("Malayalam", callback_data='ml')
	 ],
	[   InlineKeyboardButton("Maltese",callback_data = 'mt'),
        InlineKeyboardButton("Maori", callback_data='mi'),
        InlineKeyboardButton("Marathi", callback_data='mr'),
        InlineKeyboardButton("Mongolian",callback_data = 'mn')
        ],
        [   InlineKeyboardButton("Myanmar (burmese)", callback_data='my'),
        InlineKeyboardButton("Nepali", callback_data='ne')
        ],
      [  InlineKeyboardButton("Norwegian",callback_data = 'no'),
       InlineKeyboardButton("Nyanja (Chichewa)",callback_data = 'ny')
       ],
       [ InlineKeyboardButton("Odia (Oriya)",callback_data = 'or'),
	InlineKeyboardButton("Pashto", callback_data='ps'),
	InlineKeyboardButton("Persian", callback_data='fa')
	],     
	[ InlineKeyboardButton("Polish",callback_data = 'pl'),
        InlineKeyboardButton("Portuguese", callback_data='pt'),
        InlineKeyboardButton("Punjabi", callback_data='pa')
	 ],
        [InlineKeyboardButton("Romanian",callback_data = 'ro'),
         InlineKeyboardButton("Russian", callback_data='ru'),
        InlineKeyboardButton("Samoan", callback_data='sm')
	 ],
       [ InlineKeyboardButton("Scots Gaelic",callback_data = 'gd'),
         InlineKeyboardButton("Serbian", callback_data='sr'),
        InlineKeyboardButton("Sesotho", callback_data='st')
        ],
	[  InlineKeyboardButton("Shona",callback_data = 'sn'),
       InlineKeyboardButton("Sindhi", callback_data='sd'),
        InlineKeyboardButton("Sinhala", callback_data='si'),
       InlineKeyboardButton("Slovak",callback_data = 'sk')
       ],
	     [ InlineKeyboardButton("Slovenian", callback_data='sl'),
        InlineKeyboardButton("Somali", callback_data='so'),
        InlineKeyboardButton("Spanish",callback_data = 'es')
        ],
	  
        [   InlineKeyboardButton("Thai", callback_data="th"),
        InlineKeyboardButton("Turkish", callback_data="tr"),
        InlineKeyboardButton("Turkmen", callback_data="tk"),
        InlineKeyboardButton("Ukrainian",callback_data ="uk")
        ],
        [   InlineKeyboardButton("Urdu", callback_data="ur"),
        InlineKeyboardButton("Uzbek", callback_data="uz"),
        InlineKeyboardButton("Uyghur", callback_data="ug"),
        InlineKeyboardButton("Vietnamese",callback_data = "vi")
        ],
        [   InlineKeyboardButton("Welsh", callback_data="cy"),
        InlineKeyboardButton("Xhosa", callback_data="PREVIOUS_TEXT"),
        InlineKeyboardButton("Yiddish",callback_data = "vi")
        ],
        [   InlineKeyboardButton("Yoruba", callback_data="yo"),
        InlineKeyboardButton("Zulu", callback_data="zu")
        
        ]
    ]
 
 )

elif update.data == "xhosa":

        await update.message.edit_text(

            text=PREVIOUS_TEXT,

            disable_web_page_preview=True,

            reply_markup=keybord

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
