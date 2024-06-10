import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "zero",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="VEGASTRING"),
)


if __name__ == "__main__":
    print("جاري تشغيل البوت من فيجا")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("API_ID/API_HASH الخاص بك غير صالح.")
    except AccessTokenInvalid:
        raise Exception("BOT_TOKEN الخاص بك غير صالح.")
    uname = app.get_me().username
    print(f"@{uname} تم التشغيل البوت بنجاح من قبل @TopVeGa")
    idle()
    app.stop()
    print("تم ايقاف البوت بنجاح!")
