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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # parse_mode=ParseMode.MARKDOWN_V2
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hii", parse_mode=ParseMode.MARKDOWN_V2)
    # Starting the insult bot\. Your fault not mine\!
    await context.bot.send_message(chat_id=update.effective_chat.id, text="```pre-formatted fixed-width code block```", parse_mode=ParseMode.MARKDOWN_V2)
    # ```pythonpre-formatted fixed-width code block written in the Python programming language```
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[inline URL](http://www.example.com/)", parse_mode=ParseMode.MARKDOWN_V2)
    # [inline mention of a user](tg://user?id=123456789)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[inline mention of a user](tg://user?id=123456789)", parse_mode=ParseMode.MARKDOWN_V2)


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
