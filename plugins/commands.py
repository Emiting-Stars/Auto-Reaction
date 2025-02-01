from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import Config as tg
from plugins.script import *
from plugins.fsub import get_fsub

@Client.on_message(
    filters.command('start')
    & (
        filters.private |
        filters.group
    )
)
async def start_command(_, msg: Message):
    if tg.FSUB:
        client = _
        message = msg
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    return await msg.reply_photo(
        photo=tg.SB_PIC,
        caption=START_TXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Kɪᴅɴᴀᴘ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ', url=f'https://telegram.me/{tg.BOT_USERNAME}?startgroup=botstart')
                ],
                [
                    InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/EmitingStars_Botz'),
                    InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url='https://t.me/+HZuPVe0l-F1mM2Jl')
                ],
                [
                    InlineKeyboardButton('Kɪᴅɴᴀᴘ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ʙᴀʙʏ', url=f'https://telegram.me/{tg.BOT_USERNAME}?startchannel=botstart')
                ]
            ]
        ),
        parse_mode=enums.ParseMode.HTML
    )
    

@Client.on_message(
    filters.command('help')
    & (
        filters.private |
        filters.group
    )
)
async def send_emojis(_, msg: Message):
    if tg.FSUB:
        client = _
        message = msg
        is_participant = await get_fsub(client, message)
        if not is_participant:
            return
    return await msg.reply(
        text=HELP_TXT,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/EmitingStars_Botz'),
                    InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url='https://t.me/+HZuPVe0l-F1mM2Jl')
                ],[
                    InlineKeyboardButton('Cʟᴏꜱᴇ', callback_data="close")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
 
@Client.on_callback_query()
async def callback(client: Client, query: CallbackQuery): 
    if query.data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

#Emiting Stars 
#@RexySama
