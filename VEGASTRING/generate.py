from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from pyrogram import Client, filters
from pyrogram import types
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**» ▷ 𝖢𝐡𝐨𝐨𝐬𝐞 𝖳𝐡𝐞 𝖲𝐭𝐫𝐢𝐧𝐠 𝖶𝐡𝐢𝐜𝐡 𝖸𝐨𝐮 𝖶𝐚𝐧𝐭 ✔️ : :**"
buttons_ques = [
    [
        InlineKeyboardButton("𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬", callback_data="pyrogram1"),
        InlineKeyboardButton("𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬 𝖵2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬 𝖡𝖮𝖳", callback_data="pyrogram_bot"),
        InlineKeyboardButton("𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭 𝖡𝖮𝖳", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text=" 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖳𝖱𝖨𝖭𝖦 ", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "𝖳𝖤𝖫𝖤𝖳𝖧𝖮𝖭"
    else:
        ty = "𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬"
        if not old_pyro:
            ty += " 𝖵2"
    if is_bot:
        ty += " 𝖡𝖮𝖳"
    await msg.reply(f"<b>╮⦿ محاولة بدء فيجا بستخراج\n╯⦿ جلسه : {ty} لك</b>")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "<b>╮⦿ من فضلك عزيزي ارسل\n│᚜⦿ لي ᴀᴘɪ ɪᴅ الخاص بك\n╯⦿ او قم بعمل /skip </b>", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "<b>╮⦿ من فضلك عزيزي ارسل\n╯⦿ لي ᴀᴘɪ ʜᴀsʜ الخاص بك </b>", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "<b>╮⦿  عزيزي من فضلك ارسل رقم الهاتف الخاص بك\n│᚜⦿ برمز الدوله الخاصه بك\n╯⦿ هكذا : +20101236789000 </b>'"
    else:
        t = "<b>╮⦿ من فضلك عزيزي ارسل\n│᚜⦿ لي **ʙᴏᴛ_ᴛᴏᴋᴇɴ**\n╯⦿ هكذا، : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("<b>╮⦿ من فضلك عزيزي\n╯⦿ ارسل كود ᴏᴛᴩ الخاص بك</b>")
    else:
        await msg.reply(" جاري تسجيل الدخول عبر توكن البوت")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("<b>╮⦿ من فضلك عزيزي\n╯⦿ من : **ᴀᴩɪ_ɪᴅ** و **ᴀᴩɪ_ʜᴀsʜ**</b>", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply(f"<b>╮⦿ عزيزي هذا الرقم : {phone_number} \n╯⦿ لا ينتمي الي حساب في تليجرام.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ تم ارسال كود ᴏᴛᴩ \n│᚜⦿ الي رقم : {phone_number} \n│᚜⦿ تم ارسل كود ᴏᴛᴩ لك هكذا : 12345\n╯⦿ من فضلك ارسله لي هكذا 1 2 3 4 5</b>", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("<b>╮⦿ عزبزي لقد نفذ الوقت المحدد\n╯⦿ قم بالحاوله مره اخري رجاء</b>", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("<b>╮⦿ عزيزي كود OTP هذا\n╯⦿ خطاء رجاء محاوله مره اخري.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("<b>╮⦿ عزيزي كود OTP هذا\n╯⦿ منتهي الصلاحية رجاء محاوله.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "<b>╮⦿ من فضلك عزيزي يرجى إدخال\n╯⦿  كلمة مرور التحقق بخطوتين", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("<b>╮⦿ عزبزي لقد نفذ الوقت المحدد\n╯⦿ قم بالحاوله مره اخري رجاء</b>", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("<b>عزيزي كلمة المرور هذه\n╮⦿ خطاء يرجي محاوله مره اخري</b>", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ تم استخراج جلسه بنجاح\n│᚜⦿ من اصدار : {ty}\n╯⦿ هذه هي جلستك\n\n\n<code>{string_session}</code>\n\n\n╮⦿ تم استخرجها لك من\n╯⦿ <a href={MUST_JOIN}>سورس فيجا ميوزك</a>\n⦿ #ملاحظه : لا تشركها مع صديقك.</b>"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_video(
        chat_id=msg.chat.id,
        video="https://telegra.ph/file/8ef1b86bf2ece63f1d570.mp4",
        caption=f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n╮⦿ شكرا لك عزيزي لثقتك بفيجا\n╯⦿ هذه هيا جلستك : {ty} \n╮⦿ تم ارسلها لك في رسائل المحفوظه\n╯⦿ ولا تنسي الانضمام الي.<a href={MUST_JOIN}>فيجا ميوزك</a>",
        parse_mode=enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs",
                        url=f"tg://openmessage?user_id={user_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴠᴇɢᴧ", url="https://t.me/vegaone"
                    )
                ]
            ]
        )
    )









async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**تم الغاء كل العمليات بنجاح!**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**تم اعادة تشغيل بنجاح !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» 𝖢𝖠𝖭𝖢𝖤𝖫𝖫𝖤𝖣 𝖳𝖧𝖤 𝖮𝖭𝖦𝖮𝖨𝖭𝖦 𝖲𝖳𝖱𝖨𝖭𝖦 𝖲𝖤𝖲𝖲𝖨𝖮𝖭 𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖨𝖭𝖦 𝖯𝖱𝖮𝖢𝖤𝖲𝖲 !**", quote=True)
        return True
    else:
        return False
