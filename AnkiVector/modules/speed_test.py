import speedtest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, run_async

from AnkiVector import dispatcher
from AnkiVector.modules.disable import DisableAbleCommandHandler
from AnkiVector.modules.helper_funcs.chat_status import dev_plus


def convert(speed):
    return round(int(speed) / 1048576, 2)


@dev_plus
@run_async
def speedtestxyz(update: Update, context: CallbackContext):
    buttons = [
        [
            InlineKeyboardButton("🔥 SSH SSL 🔥", callback_data="sshacc_image"),
            InlineKeyboardButton("🍀 SSH SSL 🍀", callback_data="sshacc_text"),
        ]
    ]
    update.effective_message.reply_text(
        "\n🏖 23 Locations\n🔥 Unlimited Bandwith\n🚀 Fastest Servers\n🌺 100% Free\n☘@AltexSL_BOT", reply_markup=InlineKeyboardMarkup(buttons)
    )


@run_async
def speedtestxyz_callback(update: Update, context: CallbackContext):
    query = update.callback_query

  
        msg = update.effective_message.edit_text("📡 Creating Your SSH Account. . . . . . .")
        speed = speedtest.Speedtest()
        speed.get_best_server()
        speed.download()
        speed.upload()
        replymsg = "☘️ Account Created Successfully ✅\n\n🇸🇬 Singapore 🇸🇬\nᗚ  Host IP : 134.209.105.165\nᗚ  Host Name : sg.ssl.sshmonth.com\nᗚ  Port : 443 or 444\nᗚ  Username : sshmonth.com-altex430\nᗚ  Password :  sshstore\nᗚ  Expiration  : 08-January-2022\nᗚ  Max Login  : Unlimited ♾\nᗚ  Torrents  : Torrents Not Allowed ❌:"

        if query.data == "sshacc_image":
            speedtest_image = speed.results.share()
            update.effective_message.reply_photo(
                photo=speedtest_image, caption=replymsg
            )
            m45g.delete()

        elif query.data == "sshacc_text":
            result = speed.results.dict()
            replymsg = "☘️ Account Created Successfully ✅\n\n🇸🇬 Singapore 🇸🇬\nᗚ  Host IP : 134.209.105.165\nᗚ  Host Name : sg.ssl.sshmonth.com\nᗚ  Port : 443 or 444\nᗚ  Username : sshmonth.com-altex430\nᗚ  Password :  sshstore\nᗚ  Expiration  : 08-January-2022\nᗚ  Max Login  : Unlimited ♾\nᗚ  Torrents  : Torrents Not Allowed ❌"
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
