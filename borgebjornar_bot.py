from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5848871403:AAEkaZxM1G4OYRzaTexbVRvJlS97X4b1DBc",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Hello there my name is Borge Bjornar, I am a bot created by @BorgeBjornar.\n'
        'I can do a lot of things, but I am still in development. \n'
        'If you want to know what I can do, type /help')


def help(update: Update, context: CallbackContext):
    update.message.reply_text('I can do a lot of things, but I am still in development.\n'
    '\n'
    'Here is a list of commands I can do:\n'
    '/start - Start the bot again\n'
    '/help - Get help\n'
    '/linkedin - Get my LinkedIn profile')
  
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.linkedin.com/in/borgebjornar/")
  
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()