#
# Copyright (C) 2021-2022 by Logi_Help@Github, < https://github.com/LOGI-LAB >.
# @logi-channel in telegram

from config import SUPPORT_CHANNEL




from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• sᴜᴩᴩᴏʀᴛ •", url=f"https://t.me/{SUPPORT_CHANNEL}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
