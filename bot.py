from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8502462458:AAEYetCuk8koXFja-Si48yQ4p1OUicBGlyY"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot kamu sudah aktif 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

async def halo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo juga 😄")

app.add_handler(CommandHandler("halo", halo))
