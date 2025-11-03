from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread
import random
import os
import asyncio

# =============== خادم ويب منفصل =================
app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot is alive and running forever! 🚀"

@app_web.route('/ping')
def ping():
    return "pong"

def run_web_server():
    port = int(os.environ.get('PORT', 8080))
    app_web.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# ==========================================================

# الكلمات اللي يرد عليها البوت
trigger_words = ["بوبو", "بوبوو", "بوبووو"]

# الردود
bobo_replies = [
    "عيونوو",
    "قلبووووو", 
    "روح بوبوو",
    "روحووووووووووو",
    "قلبووووووووووووووو"
]

# رقمك من @userinfobot
ADMIN_ID = 806582695

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        text = update.message.text.strip().lower()

        # يرسل لك نسخة من الرسالة
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"📩 رسالة من @{update.message.from_user.username or 'بدون اسم مستخدم'}:\n{text}"
            )
        except Exception as e:
            print(f"Error sending to admin: {e}")

        # يرد على المستخدم
        if text in trigger_words:
            reply = random.choice(bobo_replies)
            await update.message.reply_text(reply)

def run_bot():
    """تشغيل البوت في thread منفصل"""
    token = os.environ.get('BOT_TOKEN', '6211628509:AAGMolj4mItGRZthCGiB55_Jz9rmNiAbeXg')
    
    async def bot_main():
        bot_app = ApplicationBuilder().token(token).build()
        bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
        
        print("البوت شغال على Render ✅")
        await bot_app.run_polling()
    
    asyncio.run(bot_main())

if __name__ == '__main__':
    # تشغيل خادم الويب في thread رئيسي
    port = int(os.environ.get('PORT', 8080))
    
    # تشغيل البوت في thread منفصل
    bot_thread = Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # تشغيل خادم الويب في thread الرئيسي
    print(f"Starting web server on port {port}")
    app_web.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
