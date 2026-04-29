from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import yt_dlp
import os
TOKEN = os.getenv("TOKEN")

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT DOWNLOAD PRO\n\n"
        "Kirim link video (TikTok / YouTube)\n\n"
        "Perintah:\n"
        "/mp3 link → download jadi MP3\n"
        "/hd link → kualitas terbaik"
    )

# ================= DOWNLOAD VIDEO =================
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    await update.message.reply_text("⏳ Sedang mendownload video...")

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'video.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        await update.message.reply_video(video=open("video.mp4", "rb"))
        os.remove("video.mp4")

    except Exception as e:
        await update.message.reply_text(f"Gagal: {e}")

# ================= DOWNLOAD HD =================
async def download_hd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = " ".join(context.args)

    await update.message.reply_text("🔥 Download kualitas tinggi...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'hd.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        await update.message.reply_video(video=open("hd.mp4", "rb"))
        os.remove("hd.mp4")

    except Exception as e:
        await update.message.reply_text(f"Gagal: {e}")

# ================= DOWNLOAD MP3 =================
async def download_mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = " ".join(context.args)

    await update.message.reply_text("🎵 Mengubah ke MP3...")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        await update.message.reply_audio(audio=open("audio.mp3", "rb"))
              os.remove("audio.mp3")

    except Exception as e:
        await update.message.reply_text(f"Gagal: {e}")

# ================= APP =================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mp3", download_mp3))
app.add_handler(CommandHandler("hd", download_hd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

app.run_polling()
