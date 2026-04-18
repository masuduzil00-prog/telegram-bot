from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

# /start command
def start(update, context):

    keyboard = [
        [InlineKeyboardButton("🎬 বাচ্চাদের ভিডিও", url="https://t.me/+AYoYy8izLuM2NmY1")],
        [InlineKeyboardButton("🧸 বাচ্চাদের গ্রুপ", url="https://t.me/bacchader_Video_viral_video")],
        [InlineKeyboardButton("🔥 Premium Group", url="https://t.me/bacchadervideo01_bot")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "👋 Welcome!\n\n"
        "🧸 বাচ্চাদের জন্য সেরা ভিডিও কালেকশন এখানে 👇\n"
        "🎬 প্রতিদিন নতুন ভিডিও আপডেট করা হয়\n\n"
        "👇 নিচের বাটনে ক্লিক করে এখনই দেখে নিন",
        reply_markup=reply_markup
    )

# BOT TOKEN (BotFather থেকে বসাবে)
updater = Updater("8703192055:AAGuF9G8DhB3qV3RbKWCBdyLqJ8VxFZTJWs", use_context=True)

# handler add
updater.dispatcher.add_handler(CommandHandler("start", start))

# start bot
updater.start_polling()
updater.idle()
