from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler
import sqlite3

# database setup
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)")
conn.commit()

def start(update, context):
    user_id = update.message.from_user.id

    # save user
    c.execute("INSERT OR IGNORE INTO users (id) VALUES (?)", (user_id,))
    conn.commit()

    # count users
    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]

    keyboard = [
        [InlineKeyboardButton("🎬 বাচ্চাদের ভিডিও", url="https://t.me/+AYoYy8izLuM2NmY1")],
        [InlineKeyboardButton("🧸 বাচ্চাদের গ্রুপ", url="https://t.me/bacchader_Video_viral_video")],
        [InlineKeyboardButton("🔥 Premium Group", url="https://t.me/bacchadervideo01_bot")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"👋 Welcome!\n\n👥 Total Users: {total_users}\n\n🧸 বাচ্চাদের ভিডিও 🎬",
        reply_markup=reply_markup
    )

updater = Updater("8703192055:AAGuF9G8DhB3qV3RbKWCBdyLqJ8VxFZTJWs", use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()

