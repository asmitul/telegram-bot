# python                    3.8
# python-telegram-bot       20.1
# pyppeteer                1.0.2


from pyppeteer import launch
import time
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

    url = update.message.text
    # await update.message.reply_photo(open("example/send_photo/example.png", 'rb'))

    browser = await launch()
    page = await browser.newPage()
    # await page.setUserAgent("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
    await page.goto(url, time=60000)
    time.sleep(10)
    await page.screenshot({'path': 'example/html_to_png/example.png', 'fullPage': False, 'clip': {'x': 0, 'y': 10, 'width': 750, 'height': 950}})
    # await page.screenshot({'path': 'example/html_to_png/example.png', 'fullPage': True})
    await browser.close()
    await update.message.reply_photo(open("example/html_to_png/example.png", 'rb'))
    os.remove("example/html_to_png/example.png")


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
