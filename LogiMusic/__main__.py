#
# Copyright (C) 2021-2022 by Logi_Help@Github, < https://github.com/LOGI-LAB >.
# @logi-channel in telegram









import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from LogiMusic import LOGGER, app, userbot
from LogiMusic.core.call import Logi
from LogiMusic.plugins import ALL_MODULES
from LogiMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("LogiMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("LogiMusic.plugins" + all_module)
    LOGGER("LogiMusic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Logi.start()
    try:
        await Logi.stream_call(
            "https://te.legra.ph/file/d5e4e6a1b6414b0d4444d.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("LogiMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Logi.decorators()
    LOGGER("LogiMusic").info("Music Bot Started Successfully ❣️")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("LogiMusic").info("Stopping Music Bot, Bhakk Bhosdike (Gaand Maraa Tu)")
