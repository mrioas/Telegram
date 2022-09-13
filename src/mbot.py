import hashlib
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


def main():
    
    print("The name of bot is: coffeyloafbot\n")
    
    f = open("token.txt","r")
    token = f.read().strip()
    #app = ApplicationBuilder().token(token).build()

    #app.add_handler(CommandHandler("hello", hello))
    #app.run_polling()
    print(token)
if "__name__" == "__main__":
    main()
