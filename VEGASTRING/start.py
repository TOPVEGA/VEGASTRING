from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await message.reply_photo(
        photo="https://telegra.ph/file/ce276acf3d3895a712914.jpg",
        caption=f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ مرحباً بك عزيزي : {msg.from_user.first_name}\n╯⦿ اسمي : {me2}\n╮⦿ تم صنعي من قبل فـيـجا\n╯⦿ اعمل علي استخراج جلسات</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖳𝖱𝖨𝖭𝖦", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ᴠᴇɢᴧ", url="https://t.me/VeGaOne"),
                    InlineKeyboardButton("Qᴜʀᴀɴ", url="https://t.me/QURANI_C")
                ]
            ]
        )
    )
