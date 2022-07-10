

import os
from pyexpat.errors import messages
import re

import yt_dlp
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaVideo, Message ,InputMediaPhoto)

from config import (BANNED_USERS, SONG_DOWNLOAD_DURATION,
                    SONG_DOWNLOAD_DURATION_LIMIT)
from strings import get_command
from LogiMusic import YouTube, app
from LogiMusic.utils.decorators.language import language, languageCB
from LogiMusic.utils.formatters import convert_bytes
from LogiMusic.utils.inline.song import song_markup

ABOUT_LOGI = get_command("ABOUT_LOGI")

@app.on_message(
    filters.command(ABOUT_LOGI)
    & filters.group
    & ~filters.edited
)
async def about_logi(client, message:Message):
    
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text= " 🦋 ᴍʏ ᴋɪɴɢ 🦋",
                    url=f"https://t.me/aboutlogesh/12",
                ),
            ]
        ]
    )
    await message.reply_text("👨‍💻**ᴀʙᴏᴜᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** \n🦋 ʜɪ ᴍʏ ɴᴀᴍᴇ ɪꜱ ʟᴏɢᴇꜱʜ \n🦋 ᴀʙᴏᴜᴛ ᴍᴇ - [ʟᴏɢᴇꜱʜ](https://t.me/aboutlogesh/12) \n🦋 ᴍʏ ᴄʜᴀɴɴᴇʟꜱ \n\n 💜 [ʟɢ ʙᴏᴛꜱ](https://t.me/LGbots) \n💜 [ʟᴏɢɪ ᴄʜᴀɴɴᴇʟ](https://t.me/LOGI_CHANNEL)\n💜 [ʜᴀᴄᴋᴇʀ x](https://t.me/hacker_x_x)\nᴛʜᴀɴᴋꜱ ꜰᴏʀ ʀᴇᴀᴅ ɪᴛ ❤ ", reply_markup=upl)
    await InputMediaPhoto.media("https://te.legra.ph/file/fc96390beb168c19b1788.jpg")
    



