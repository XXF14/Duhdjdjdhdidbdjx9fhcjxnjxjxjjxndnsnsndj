

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import db
from pyromod.exceptions import ListenerTimeout
from config import rkn

TRUE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏɴ', callback_data='metadata_1'),
       InlineKeyboardButton('✅', callback_data='metadata_1')
       ],[
       InlineKeyboardButton('Sᴇᴛ Cᴜsᴛᴏᴍ Mᴇᴛᴀᴅᴀᴛᴀ', callback_data='cutom_metadata')]]
FALSE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏғғ', callback_data='metadata_0'),
        InlineKeyboardButton('❌', callback_data='metadata_0')
       ],[
       InlineKeyboardButton('Sᴇᴛ Cᴜsᴛᴏᴍ Mᴇᴛᴀᴅᴀᴛᴀ', callback_data='cutom_metadata')]]

@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    RknDev = await message.reply_text("**Please Wait...**", reply_to_message_id=message.id)
    bool_metadata = await db.get_metadata_mode(message.from_user.id)
    user_metadata = await db.get_metadata_code(message.from_user.id)
    if bool_metadata:
        return await RknDev.edit(f"Your Current Metadata:-\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(TRUE))
    return await RknDev.edit(f"Your Current Metadata:-\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(FALSE))

@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    data = query.data
    if data.startswith('metadata_'):
        _bool = data.split('_')[1]
        user_metadata = await db.get_metadata_code(query.from_user.id)
        if bool(eval(_bool)):
            await db.set_metadata_mode(query.from_user.id, bool_meta=False)
            await query.message.edit(f"Your Current Metadata:-\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(FALSE))
        else:
            await db.set_metadata_mode(query.from_user.id, bool_meta=True)
            await query.message.edit(f"Your Current Metadata:-\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(TRUE))

    elif data == 'cutom_metadata':
        await query.message.delete()
        try:
            try:
                metadata = await bot.ask(text=rkn.SEND_METADATA, chat_id=query.from_user.id, filters=filters.text, timeout=30, disable_web_page_preview=True)
            except ListenerTimeout:
                await query.message.reply_text("⚠️ Error!!\n\n**Request timed out.**\nRestart by using /metadata", reply_to_message_id=query.message.id)
                return
            print(metadata.text)
            RknDev = await query.message.reply_text("**Please Wait...**", reply_to_message_id=metadata.id)
            await db.set_metadata_code(query.from_user.id, metadata_code=metadata.text)
            await RknDev.edit("**Your Metadta Code Set Successfully ✅**")
        except Exception as e:
            print(e)

