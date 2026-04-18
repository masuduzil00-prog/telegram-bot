from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🎬 বাচ্চাদের ভিডিও", url="https://t.me/+AYoYy8izLuM2NmY1")],
        [InlineKeyboardButton("🧸 বাচ্চাদের গ্রুপ", url="https://t.me/bacchader_Video_viral_video")],
        [InlineKeyboardButton("🔥 Premium Group", url="https://t.me/bacchadervideo01_bot")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "👋 Welcome!\n\n🧸 বাচ্চাদের ভিডিও এখানে 🎬\n👇 নিচে ক্লিক করুন",
        reply_markup=reply_markup
    )

updater = Updater("8703192055:AAGuF9G8DhB3qV3RbKWCBdyLqJ8VxFZTJWs", use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()  
