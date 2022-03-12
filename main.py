from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from telegram.ext.messagequeue import queuedmessage
import os
from dotenv import load_dotenv
import datetime

import Calendar.calendar as gcAPI
import events_calendar as gcEvents

load_dotenv('ignore/.env')

TOKEN = os.getenv("TOKEN_BOT")
CHAT = os.getenv("CHAT_ID")


def informacao(update, context):
    message = "Welcome to Baracusbot. I have a goal, help you with dates of "
    message += "jobs and tests during your university.\n"
    message += "You can write the command schedule, and i will show the 10"
    message += "next events in your calendar."

    update.message.reply_text(message)

def calendarAPI(update, context):
    message = update.message

    events = gcAPI.main()
    
    if not events:
        message.reply_text("There isn't event in your calendar")
        return

    list_events = list(map(gcEvents.extract_event_info, events))
    message_to_reply = ""
    for event in list_events:
        data_begin = event.start
        data_end = event.end
        summary = event.summary

        data_begin, time_begin = gcEvents.extrac_data(data_begin)
        data_end, time_end = gcEvents.extrac_data(data_end)

        message_to_reply += f"{summary}: {data_begin} às {time_begin} --> {data_end} às {time_end}\n\n"

    message.reply_text(message_to_reply)

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig (
        format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO
    )

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("info", informacao))
    dp.add_handler(CommandHandler("schedule", calendarAPI))

    updater.start_polling()
    logging.info("=== Bot running! ===")
    updater.idle()
    logging.info("=== Bot shutting down! ===")

if __name__ == "__main__":
    main()