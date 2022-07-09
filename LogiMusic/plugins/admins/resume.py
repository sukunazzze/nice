#
# Copyright (C) 2021-2022 by Logi_Help@Github, < https://github.com/LOGI-LAB >.
# @logi-channel in telegram





from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from LogiMusic import app
from LogiMusic.core.call import Logi
from LogiMusic.utils.database import is_music_playing, music_on
from LogiMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Logi.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention)
    )
