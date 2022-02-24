import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_massages(message):
    username = message.from_user.username
    msg = f"Привет, {username}"
    bot.send_message(message.from_user.id, msg)


bot.polling()


