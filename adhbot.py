from telegram.ext import Updater, CommandHandler

# ✅ Replace with your real bot token
BOT_TOKEN = "8273206202:AAFHz0kWQaOmduMRZiyitrrbHZvkTwzNT2E"

# ✅ Replace with your ShrinkEarn link
SHORT_LINK = "https://tpi.li/Android_Dev_Hub"

def start(update, context):
    update.message.reply_text("👋 Welcome to Android Dev Hub Bot!\nUse /file to get the latest File.")

def send_zip(update, context):
    message = (
        "🎁 *From:* YouTube\n"
        "🔽*Pass:* In YouTube Video\n\n"
        "👉👉 [💾 Download](https://tpi.li/Android_Dev_Hub)👈👈"
    )
    update.message.reply_text(message, parse_mode='Markdown', disable_web_page_preview=True)

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

# Commands
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("file", send_zip))

# Start the bot
updater.start_polling()
updater.idle()