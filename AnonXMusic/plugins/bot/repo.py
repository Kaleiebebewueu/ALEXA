from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app

start_txt = """<b>
❖ ᴡᴏʀᴋ ɪs ɪɴ ᴘʀᴏɢʀᴇss ᴏɴ ᴛʜɪs ʙᴏᴛ

❖ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴛᴏ ʟɪsᴛᴇɴ ᴛᴏ ᴍᴜsɪᴄ

▷ @HIMANSHI_MUSIC_BOT

❍ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ 💌 </b>
"""

@app.on_message(filters.command("play"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("• ʌᴅᴅ ᴍᴇ ɪɴ ʏσᴜʀ ɢʀσᴜᴘ •", url="https://t.me/HIMANSHI_MUSIC_BOT?startgroup=true")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/79547e01862628bb85df0.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
