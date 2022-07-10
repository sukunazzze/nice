
from strings import get_command
from pyrogram import filters
from LogiMusic import app

ABOUT_LOGI = get_command("ABOUT_LOGI")

@app.on_message(
    filters.command(ABOUT_LOGI)
    & filters.group
    & ~filters.edited
)

def about_logi():

 """👨‍💻**<u>🅰🅱🅾🆄🆃 🅲🆁🅴🅰🆃🅾🆁 :</u>**
🦋 ʜɪ ᴍʏ ɴᴀᴍᴇ ɪꜱ ʟᴏɢᴇꜱʜ ,
🦋 ᴀʙᴏᴜᴛ ᴍᴇ - [ʟᴏɢᴇꜱʜ](https://t.me/aboutlogesh/12)
🦋 ᴍʏ ᴄʜᴀɴɴᴇʟꜱ :
                    💜 [ʟɢ ʙᴏᴛꜱ](https://t.me/LGbots) 
                    💜 [ʟᴏɢɪ ᴄʜᴀɴɴᴇʟ](https://t.me/LOGI_CHANNEL)
                    
                    💜 [ʜᴀᴄᴋᴇʀ x](https://t.me/hacker_x_x)
                     ᴛʜᴀɴᴋꜱ ꜰᴏʀ ʀᴇᴀᴅ ɪᴛ ❤
"""