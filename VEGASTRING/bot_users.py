from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID
from VEGASTRING.db.users import add_served_user, get_served_users

SUDORS = [OWNER_ID]

@Client.on_message(filters.command(["/start"], "") & filters.private)
async def kep(client, msg):
    if msg.from_user.id in SUDORS:
        kep = ReplyKeyboardMarkup([["قسم فيجا"], ["قسم الاذاعه"], ["قسم البوت","قسم المساعد"], ["التواصل و الاحصائيات"], ["النسخه الاحتياطيه"], ["الاشتراك الاجباري"], ["بينج","تنظيف"], ["الكولات النشطه","الفيديوهات النشطه"], ["تعليمات"], ["قفل الكيبورد"]], resize_keyboard=True)
        await msg.reply_text("<b>╮✪ مـرحـبآ بڪ عزيـزي المطـور الاساسـي\n╯✪ اليك كيب التحكم بالبوت من فيجا</b>", reply_markup=kep)
        

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)


@Client.on_message(filters.command(["الاحصائيات"], "") & filters.private)
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)


