#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from ..functions.filters import Filter
from .. import client


@Client.on_message(filters.private & filters.command("help") & Filter.auth_users)
async def help(bot: Client, update: Message):
    await bot.send_message(
        chat_id=update.chat.id,
        text=client.translation.HELP_USER,
        disable_web_page_preview=True,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.private & filters.command("start") & Filter.auth_users)
async def start(bot: Client, update: Message):
    await bot.send_message(
        chat_id=update.chat.id,
        text=client.translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                    InlineKeyboardButton(
                        "🔪🖤 ᴰᵉᵛˡᵒᵖᵉʳ ", url="https://t.me/X_XF8"
                    ),
                    InlineKeyboardButton(
                        "𝙼𝚢 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url="https://t.me/MOVIES0X1"),
                ],
                [InlineKeyboardButton("🏴🤍 𝙵𝙾𝙻𝙻𝙾𝚆 𝙼𝙴 𝙾𝙽 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺", url="https://www.facebook.com/x.hetlr.7")],
            ]
        ),
        reply_to_message_id=update.id
    )
