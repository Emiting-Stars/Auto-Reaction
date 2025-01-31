from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from config import Config

@Client.on_message(filters.all)
async def send_reaction(_, msg: Message):
    try:
        await msg.react(choice(Config.EMOJIS))
    except (
        MessageIdInvalid,
        EmoticonInvalid,
        ChatAdminRequired,
        ReactionInvalid
    ):
        pass
