from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread
import random
import os

# ================== خادم Render (لبقاء التطبيق شغال) ==================
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "✅ Bot is alive and running!"

def run():
    # استخدم المنفذ اللي يرسله Render
    port = int(os.environ.get("PORT", 8080))
    app_web.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
# ======================================================================

# الكلمات اللي يرد عليها البوت
trigger_words = ["بوبو", "بوبوو", "بوبووو"]

# الردود المحتملة
bobo_replies = [
    "عيونوو",
    "قلبووووو",
    "روح بوبوو",
    "روحووووووووووو",
    "قلبووووووووووووووو"
]

# رقمك من @userinfobot
ADMIN_ID = 806582695  # ← غيّره إذا تبغى

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.strip().lower()

        # يرسل لك نسخة من الرسالة
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"📩 رسالة من @{update.message.from_user.username or 'بدون اسم مستخدم'}:\n{text}"
            )
        except:
            pass

        # يرد على المستخدم
        if text in trigger_words:
            reply = random.choice(bobo_replies)
            await update.message.reply_text(reply)

# تشغيل السيرفر والبوت
keep_alive()

print("🚀 البوت يبدأ الآن...")

bot_app = ApplicationBuilder().token("6211628509:AAGMolj4mItGRZthCGiB55_Jz9rmNiAbeXg").build()
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

bot_app.run_polling()
