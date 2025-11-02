from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import random

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

# حط هنا رقمك اللي طلع من @userinfobot
ADMIN_ID = 123456789  # ← استبدله برقمك

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        text = update.message.text.strip().lower()

        # يرسل لك نسخة من الرسالة على الخاص
        try:
            await context.bot.send_message(
                chat_id=806582695,
                text=f"📩 رسالة من @{update.message.from_user.username or 'بدون اسم مستخدم'}:\n{text}"
            )
        except:
            pass  # يتجاهل لو ما قدر يرسل

        # يرد على المستخدم
        if text in trigger_words:
            reply = random.choice(bobo_replies)
            await update.message.reply_text(reply)

app = ApplicationBuilder().token("6211628509:AAGMolj4mItGRZthCGiB55_Jz9rmNiAbeXg").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

print("البوت شغال ✅")
app.run_polling()
