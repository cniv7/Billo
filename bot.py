from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread
import random
import os
import asyncio

# خادم ويب بسيط
app = Flask('')

@app.route('/')
def home():
    return "🤖 البوت شغال على Render! ✅"

@app.route('/ping')
def ping():
    return "pong"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# إعدادات البوت
trigger_words = ["بوبو", "بوبوو", "بوبووو"]
bobo_replies = [
    "عيونوو",
    "قلبووووو", 
    "روح بوبوو",
    "روحووووووووووو",
    "قلبووووووووووووووو"
]

ADMIN_ID = 806582695

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        text = update.message.text.strip().lower()

        # يرسل نسخة من الرسالة للإدمن
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"📩 رسالة من @{update.message.from_user.username or 'بدون اسم مستخدم'}:\n{text}"
            )
        except Exception as e:
            print(f"Error sending to admin: {e}")

        # يرد إذا كانت الكلمة من trigger_words
        if text in trigger_words:
            reply = random.choice(bobo_replies)
            await update.message.reply_text(reply)

async def main():
    # احصل على التوكن
    token = os.environ.get('BOT_TOKEN', '6211628509:AAGMolj4mItGRZthCGiB55_Jz9rmNiAbeXg')
    
    # أنشئ البوت
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ البوت شغال على Render! جرب أرسل 'بوبو'")
    await application.run_polling()

if __name__ == '__main__':
    # شغّل خادم الويب في thread منفصل
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # شغّل البوت
    asyncio.run(main())
