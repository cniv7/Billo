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

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        text = update.message.text.strip().lower()
        if text in trigger_words:
            reply = random.choice(bobo_replies)
            await update.message.reply_text(reply)

app = ApplicationBuilder().token("6211628509:AAGMolj4mItGRZthCGiB55_Jz9rmNiAbeXg").build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

print("البوت شغال ✅")
app.run_polling()