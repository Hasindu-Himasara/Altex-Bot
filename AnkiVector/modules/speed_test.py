import speedtest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, run_async

from AnkiVector import DEV_USERS, dispatcher
from AnkiVector.modules.disable import DisableAbleCommandHandler
from AnkiVector.modules.helper_funcs.chat_status import dev_plus


def convert(speed):
    return round(int(speed) / 1048576, 2)


@dev_plus
@run_async
def speedtestxyz(update: Update, context: CallbackContext):
    buttons = [
        [
            InlineKeyboardButton("🔥 Create SSH SSL 🔥", callback_data="sshacc_image"),
            InlineKeyboardButton("🍀 Genarate V2ray 🍀", callback_data="sshacc_text"),
        ]
    ]
    update.effective_message.reply_text(
        "\n🏖 23 Locations\n🔥 Unlimited Bandwith\n🚀 Fastest Servers\n🌺 100% Free\n☘@AltexSL_BOT", reply_markup=InlineKeyboardMarkup(buttons)
    )


@run_async
def speedtestxyz_callback(update: Update, context: CallbackContext):
    query = update.callback_query

    if query.from_user.id in DEV_USERS:
        msg = update.effective_message.edit_text("📡 Creating Your SSH Account. . . . . . .")
        speed = speedtest.Speedtest()
        speed.get_best_server()
        speed.download()
        speed.upload()
        replymsg = "☘️ Account Created Successfully ✅\n\n🇸🇬 Singapore 🇸🇬\nᗚ Host IP : sg-fullv2ray.racevpn.com\nᗚ Port : 443\nᗚ Max Login : ✅\n🎮 Best For Gaming 🎮\n\nᗚ V2ray Link : `vless://e0480f5c-4e78-4efe-8d83-b8d0affb2ff7@sg-fullv2ray.racevpn.com:443?type=tcp&encryption=none&security=xtls&path=%2f&headerType=none&flow=xtls-rprx-direct#🇸🇬-Singapore-🇸🇬-XTLS-☘️-The-SSH-Store-`☘️\n\n💖 @AltexSL_BOT:"

        if query.data == "sshacc_image":
            speedtest_image = speed.results.share()
            update.effective_message.reply_photo(
                photo=speedtest_image, caption=replymsg
            )
            msg.delete()

        elif query.data == "sshacc_text":
            result = speed.results.dict()
            replymsg += "🇸🇬 Singapore 🇸🇬\n\nᗚ Host IP : sg-fullv2ray.racevpn.com\nᗚ Port : 443\nᗚ Max Login : ✅\n🎮 Best For Gaming 🎮\n\nᗚ V2ray Link : `vless://e0480f5c-4e78-4efe-8d83-b8d0affb2ff7@sg-fullv2ray.racevpn.com:443?type=tcp&encryption=none&security=xtls&path=%2f&headerType=none&flow=xtls-rprx-direct#🇸🇬-Singapore-🇸🇬-XTLS-☘️-The-SSH-Store-`☘️\n\n💖 @AltexSL_BOT"
            update.effective_message.edit_text(replymsg, parse_mode=ParseMode.MARKDOWN)
    else:
        query.answer("You are required to join Heroes Association to use this command.")


SPEED_TEST_HANDLER = DisableAbleCommandHandler("sshacc", speedtestxyz)
SPEED_TEST_CALLBACKHANDLER = CallbackQueryHandler(
    speedtestxyz_callback, pattern="sshacc_.*"
)

dispatcher.add_handler(SPEED_TEST_HANDLER)
dispatcher.add_handler(SPEED_TEST_CALLBACKHANDLER)

__mod_name__ = "☘ SSH ☘"
__command_list__ = ["sshacc"]
__handlers__ = [SPEED_TEST_HANDLER, SPEED_TEST_CALLBACKHANDLER]
