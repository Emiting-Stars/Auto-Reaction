from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config as tg


async def get_fsub(bot, message):
    target_channel_id = tg.FSUB_ID  # Your channel ID
    user_id = message.from_user.id
    try:
        await bot.get_chat_member(target_channel_id, user_id)
    except UserNotParticipant:
        channel_link = (await bot.get_chat(target_channel_id)).invite_link
        join_button = InlineKeyboardButton("Join Channel", url=channel_link)
        keyboard = [[join_button]]
        await message.reply(
            f"<b>Dᴇᴀʀ Usᴇʀ {message.from_user.mention}!\n\n<blockquote>Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊</blockquote>\n\n<blockquote expandable>Tʜᴇ sᴛʀᴏɴɢ sʜᴏᴜʟᴅ ᴀɪᴅ ᴀɴᴅ ᴘʀᴏᴛᴇᴄᴛ ᴛʜᴇ ᴡᴇᴀᴋ. ᴛʜᴇɴ, ᴛʜᴇ ᴡᴇᴀᴋ ᴡɪʟʟ ʙᴇᴄᴏᴍᴇ sᴛʀᴏɴɢ, ᴀɴᴅ ᴛʜᴇʏ ɪɴ ᴛᴜʀɴ ᴡɪʟʟ ᴀɪᴅ ᴀɴᴅ ᴘʀᴏᴛᴇᴄᴛ ᴛʜᴏsᴇ ᴡᴇᴀᴋᴇʀ ᴛʜᴀɴ ᴛʜᴇᴍ. ᴛʜᴀᴛ ɪs ᴛʜᴇ ʟᴀᴡ ᴏғ ɴᴀᴛᴜʀᴇ.</blockquote>\n<blockquote>Pᴏᴡᴇʀᴇᴅ ʙʏ @EmitingStars_Botz</blockquote></b>",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return False
    else:
        return True

#Emiting Stars 
#@RexySama
