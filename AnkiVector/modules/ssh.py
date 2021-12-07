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
            InlineKeyboardButton("SSH.....", callback_data="speedtest_image"),
            InlineKeyboardButton("SSH.....", callback_data="speedtest_text"),
        ]
    ]
    update.effective_message.reply_text(
        "Select SpeedTest Mode", reply_markup=InlineKeyboardMarkup(buttons)
    )
