from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask
from threading import Thread
import random
import os
import logging

# إعداد اللوجر
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

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

def reply_message(update: Update, context: CallbackContext):
    if update.message.chat.type == "private":
        text = update.message.text.strip().lower()
        
        # يرسل نسخة من الرسالة للإدمن
        try:
            context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"📩 رسالة من @{update.message.from_user.username or 'بدون اسم مستخدم'}:\n{text}"
            )
        except Exception as e:
            logger.error(f"Error sending to admin: {e}")

        # يرد إذا كانت الكلمة من trigger_words
        if text in trigger_words:
            reply = random.choice(bobo_replies)
            update.message.reply_text(reply)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('مرحباً! أنا بوت شغال على Render 🚀')

def main():
    # احصل على التوكن
    token = os.environ.get('BOT_TOKEN', '6211628509:AAGMolj4mItGRZthCGiB55_Jz9rmNiAbeXg')
    
    # أنشئ البوت
    updater = Updater(token, use_context=True)
    
    # أضف handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))
    
    # ابدأ البوت
    updater.start_polling()
    logger.info("✅ البوت شغال الحين! جرب أرسل 'بوبو'")
    
    # اجعل البوت يشتغل إلى ما لا نهاية
    updater.idle()

if __name__ == '__main__':
    # شغّل خادم الويب في thread منفصل
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # شغّل البوت
    main()
