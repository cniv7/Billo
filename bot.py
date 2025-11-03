from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread
import random
import os
import time

# خادم بسيط علشان يفضل البوت شغال
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive! ✅"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# شغّل Flask في thread منفصل
Thread(target=run_flask, daemon=True).start()

# إعدادات البوت
trigger_words = ["بوبو", "بوبوو", "بوبووو"]
bobo_replies = ["عيونوو", "قلبووووو", "روح بوبوو", "روحووووووووووو", "قلبووووووووووووووو"]
ADMIN_ID = 806582695

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        text = update.message.text.strip().lower()

        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"📩 رسخة من @{update.message.from_user.username or 'بدون اسم مستخدم'}:\n{text}"
            )
        except Exception as e:
            print(f"Error: {e}")

        if text in trigger_words:
            reply = random.choice(bobo_replies)
            await update.message.reply_text(reply)

def main():
    token = os.environ.get('BOT_TOKEN', '6211628509:AAGMolj4mItGRZthCGiB55_Jz9rmNiAbeXg')
    
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))
    
    print("🎉 البوت شغال الحين! جرب أرسل 'بوبو'")
    app.run_polling()

if __name__ == '__main__':
    main()
