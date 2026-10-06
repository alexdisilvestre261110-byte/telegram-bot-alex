import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Attiva il sistema di log per vedere gli eventi in console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Legge il token di Telegram dalle variabili d'ambiente
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Funzione che risponde al comando /ciao
async def ciao_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao, sono Xela")

if __name__ == '__main__':
    if not TELEGRAM_TOKEN:
        raise ValueError("ERRORE: La variabile d'ambiente TELEGRAM_TOKEN non è impostata!")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Collega il comando /ciao alla funzione ciao_command
    app.add_handler(CommandHandler("ciao", ciao_command))

    print("Bot avviato e in ascolto...")
    app.run_polling()
