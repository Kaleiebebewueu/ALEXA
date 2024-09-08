from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app 

@app.on_message(filters.group)
async def delete_edited_message(client, message):
    if message.edit_date:
        try:

            await message.delete()

            close_button = InlineKeyboardMarkup([
                [InlineKeyboardButton("Close", callback_data="close_warning")]
            ])

            warning_text = f"{message.from_user.mention}, please do not edit your messages!"
            await message.reply_text(warning_text, reply_markup=close_button)

        except Exception as e:
            print(f"Error: {e}")


@app.on_callback_query(filters.regex("close_warning"))
async def close_warning_message(client, callback_query):
    try:
        await callback_query.message.delete()
        await callback_query.answer()
    except Exception as e:
        print(f"Error: {e}")
