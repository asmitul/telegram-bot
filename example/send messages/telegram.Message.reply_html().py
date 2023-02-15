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

    # await context.bot.send_message(chat_id=update.effective_chat.id, text="<a href='https://www.w3schools.com'>Visit W3Schools.com! goooooooooooo</a>", parse_mode=ParseMode.HTML)
    # <button type="button" onclick="alert('Hello world!')">Click Me!</button>
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="<button type='button' onclick='alert('Hello world!')'>Click Me!</button>", parse_mode=ParseMode.HTML)
    # <p><b>This text is bold</b></p><p><i>This text is italic</i></p><p>This is<sub> subscript</sub> and <sup>superscript</sup></p>
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hii", parse_mode=ParseMode.HTML)
    # <b>This text is bold.</b>
    await context.bot.send_message(chat_id=update.effective_chat.id, text="<b>This text is bold.</b>", parse_mode=ParseMode.HTML)
    # <strong> - Important text
    await context.bot.send_message(chat_id=update.effective_chat.id, text="<strong>This text is Important text</strong>", parse_mode=ParseMode.HTML)
    # <i> - Italic text
    await context.bot.send_message(chat_id=update.effective_chat.id, text="<i>This text is Italic text</i>", parse_mode=ParseMode.HTML)
    # <em> - Emphasized text
    await context.bot.send_message(chat_id=update.effective_chat.id, text="<em>This text is Emphasized text</em>", parse_mode=ParseMode.HTML)
    # My favorite color is <del>blue</del> red.
    await context.bot.send_message(chat_id=update.effective_chat.id, text="My favorite color is <del>blue</del> <ins>red</ins>.", parse_mode=ParseMode.HTML)
    # <pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
    await context.bot.send_message(chat_id=update.effective_chat.id, text="<pre><code class='language-python'>pre-formatted fixed-width code block written in the Python programming language</code></pre>", parse_mode=ParseMode.HTML)


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
