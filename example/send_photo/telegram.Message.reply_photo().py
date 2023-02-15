# await bot.send_photo(update.effective_chat.id, *args, **kwargs)

# async send_message(text, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None, allow_sending_without_reply=None, entities=None, protect_content=None, message_thread_id=None, *, read_timeout=None, write_timeout=None, connect_timeout=None, pool_timeout=None, api_kwargs=None)

# await bot.send_message(update.effective_chat.id, *args, **kwargs)

# python 3.8
# python-telegram-bot 20.1

from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# That will print the current working directory along with all the files in it.

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # https://imgur.com/Pbtrt1V
    # await update.message.reply_photo(photo="https://imgur.com/Pbtrt1V")
    # C:\Users\Gabriel\OneDrive\Documents\GitHub-as\telegram-bot\example\send_photo\example.png
    # await update.message.reply_photo(open("C:/Users/Gabriel/OneDrive/Documents/GitHub-as/telegram-bot/example/send_photo/example.png", 'rb'))
    await update.message.reply_photo(open("example/send_photo/example.png", 'rb'))


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    # replace you bot_token in .env
    application = Application.builder().token(
        BOT_TOKEN).build()

    # Interpret any other command or text message as a start of a private chat.
    # This will record the user as being in a private chat with bot.
    application.add_handler(MessageHandler(filters.ALL, start))

    # Run the bot until the user presses Ctrl-C
    # We pass 'allowed_updates' handle *all* updates including `chat_member` updates
    # To reset this, simply pass `allowed_updates=[]`
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
