

from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def detect_type(m: Message):
    if m.document:
        return m.document
    elif m.video:
        return m.video
    elif m.audio:
        return m.audio
    else:
        return
    

@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4)
async def media_receive_handler(_, m: Message):
    file = detect_type(m)
    file_name = ''
    if file:
        file_name = file.file_name
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = Var.URL + str(log_msg.message_id) + '/' +quote_plus(file_name) if file_name else ''
    stream_links = f"https://www.trendingtips.in/"
    await m.reply_text(
        text=f"https://aklinks2.000webhostapp.com/st?api=d77571ad7bab5ebf5e07b86514a5591bb9dcdb0f&url={stream_link}",
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Learn something interesting 🤔', url=stream_links)]])
    )
