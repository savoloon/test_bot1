import telebot

bot = telebot.TeleBot('5183745281:AAHxc5o1_VjgqPk0_GkXOe-NJH8iEeBSij0')


@bot.message_handler(content_types=['text'])
def get_text_massages(message):
    bot.send_message(message.from_user.id, f"Кто здесь")



