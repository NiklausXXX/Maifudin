import os
import asyncio
import time
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, CallbackQuery


bot = Client(
    "Superman Alpha Bot",
    api_id = 10980915,
    api_hash = '035b931bbf6ab787071dfc0e146530f3',
    bot_token = '5282944537:AAHjJk4Ut3kEFXCteLYIBVMh5ZsTzHS7Meg'
    )

MONGO_URI = 'mongodb+srv://superman:Bawel12345@superxxly.ykpp6as.mongodb.net/?retryWrites=true&w=majority'

START_MESSAGE = "Bukan burung! bukan pesawat! tapi, superman."
START_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton("•Menu•", callback_data="menu"),
        InlineKeyboardButton("•Help•", callback_data="help")
        ],
    [
        InlineKeyboardButton("•Owner•", url="https://t.me/superxxly")
        ]
    ]
    
MAIFAM_MENU_BUTTON = [
    [
        InlineKeyboardButton("•Achievement•", callback_data="acv"),
        InlineKeyboardButton("Exclusive Item", callback_data="magic")
        ],
        [
            InlineKeyboardButton("•Back•", callback_data="BACK1")
                ]
        ]

@bot.on_message(filters.command('start'))
def start(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.text & filters.private)
def echobot(client, message):
    message.reply_text(f"Kamu bilang {message.text}." )

GROUP = 'maifudin'
WELCOME_MESSAGE = """
Halo, Selamat Datang!
Jangan Keluar 😉
"""
HELP_MESSAGE = """**Help Menu**

#StartMenu
■**Menu**
  __Untuk memulai membuka Menu Utama__

■**Help**
  __Tampilan ini, berisi tentang Bantuan__
  
■**Owner**
  __Berisi informasi mengenai pemilik bot__

#MaifamMenu
■**Achievement**
  __Informasi mengenai barang-barang yang bisa mendapatkan 💎Gem jika dijual__
  
■**Exclusive Item**
  __Berisi informasi mengenai item-item Exclusive__

"""
ACV_MESSAGE = "⚙️COMING SOON"
MAGIC_MESSAGE = "⚙️COMING SOON"

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcome(client, message):
    message.reply_text(WELCOME_MESSAGE)
    
@bot.on_message(filters.command('leave') & filters.group)
def leave_mesaage(bot, message):
    bot.send_message(message.chat.id, "Dadah semua👋, aku sudah cringe 😔")
    bot.leave_chat(message.chat.id)
    
@bot.on_message(filters.command('ban') & filters.group)
def ban_user(bot, message):
    bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"Mampus! (message.reply_to_message.from_user.mention) telah di Banned.")
    
@bot.on_message(filters.command('unban') & filters.group)
def unban_user(bot, message):
    bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"Karena Kasihan, (message.reply_to_message.from_user.mention) telah di unbanned.")

@bot.on_message(filters.command('mute') & filters.group)
def mute(bot, message):
    bot.restrict_user(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions)
    bot.send_message(message.chat.id, f"Mampus! (message.reply_to_message.from_user.mention) telah di Mute.")

#Callback Query
@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "menu":
        MENU_MESSAGE = """**Menu Utama by Superman**

■**Maifam Menu**
  __Menampilkan informasi berkaitan dengan Maifam__

■**Music (Sedang dalam perbaikan ...)**
  __Menampilkan musik-musik enak by Superman__

■**Coming Soon..**
  __Kamu bisa request Menu yang kamu inginkan__
  __Cukup kirim: #ReqMenu NamaMenu-FungsiMenu kirim ke Group Kami @maifudin.__
        """
        MENU_BUTTON = [
            [
                InlineKeyboardButton("•Maifam•", callback_data="maifam"),
                InlineKeyboardButton("•Musik•", callback_data="magic")
            ],
            [
                InlineKeyboardButton("•Back•", callback_data="BACK")
                ]
            ]
            
        CallbackQuery.edit_message_text(
            MENU_MESSAGE,
            reply_markup = InlineKeyboardMarkup(MENU_BUTTON)
        )
        
    if CallbackQuery.data == "maifam":
        MAIFAM_MENU_MESSAGE = """**Maifam Menu**

■**Achievement Data**
  __Cek Item-item Achievement pada Maifam__

■**Exclusive Item**
  __Cek Informasi tentang Batu Sihir (Lab), Batu Sihir Loak, Batu Sihir Ekslusif__
"""
        MAIFAM_MENU_BUTTONS = [
            [
                InlineKeyboardButton("•Achievement•", callback_data="acv"),
                InlineKeyboardButton("Exclusive Item", callback_data="magic")
            ],
            [
                InlineKeyboardButton("•Back•", callback_data="BACK1")
                ]
            ]
        CallbackQuery.edit_message_text(
            MAIFAM_MENU_MESSAGE,
            reply_markup = InlineKeyboardMarkup(MAIFAM_MENU_BUTTONS)
            )
        
    if CallbackQuery.data == "acv":
        MENU_ACV_BUTTON = [
            [
                InlineKeyboardButton("•Hasil Buru•", callback_data="hewan"),
                InlineKeyboardButton("•Hasil Tanam•", callback_data="farm")
                ],
                [
                    InlineKeyboardButton("•Mineral•", callback_data="mine"),
                    InlineKeyboardButton("•Hasil Ternak•", callback_data="ternak")
                    ],
                [
                    InlineKeyboardButton("•Hasil Pancing•", callback_data="ikan")
                    ],
                [
                    InlineKeyboardButton("•Maifam Menu", callback_data="maifam")
                    ]
            ]
        CallbackQuery.edit_message_text(
            ACV_MESSAGE,
            reply_markup = InlineKeyboardMarkup(MENU_ACV_BUTTON)
            )
    
    elif CallbackQuery.data == "help":
        BACK_BUTTON = [
            [
                InlineKeyboardButton("•Back•", callback_data="BACK")
                ]
            ]
        CallbackQuery.edit_message_text(
            HELP_MESSAGE,
            reply_markup = InlineKeyboardMarkup(BACK_BUTTON)
            )
    
    elif CallbackQuery.data == "BACK":
        CallbackQuery.edit_message_text(
            START_MESSAGE,
            reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
            )
    elif CallbackQuery.data == "BACK1":
        MAIFAM_MENU_MESSAGE = """**Maifam Menu**

■**Achievement Data**
  __Cek Item-item Achievement pada Maifam__

■**Exclusive Item**
  __Cek Informasi tentang Batu Sihir (Lab), Batu Sihir Loak, Batu Sihir Ekslusif__
"""
        BACK_TO_MAIFAM_BUTTON = [
            [
                InlineKeyboardButton("•Back•", callback_data="BACK1")
                ]
            ]
        CallbackQuery.edit_message_text(
            MAIFAM_MENU_MESSAGE,
            reply_markup = InlineKeyboardMarkup(BACK_TO_MAIFAM_BUTTON)
            )



print("GW ONLINE")
bot.run()

