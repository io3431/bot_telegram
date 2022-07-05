import telebot
from telebot import types

from search_raspisanie import file_writer, take_last_posts

token = '5257001198:AAFq7YsRJdZ-By1rBZFZ73-3Hh28tJgdXO8'

bot = telebot.TeleBot(token)

MESS_MAX_LENGHT = 4096


def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Расписание")

    markup.add(item)

    bot.send_message(message.chat.id, "Расписание:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def msg(message):
    if message.chat.type == 'private':
        if message.text == 'Расписание':
            text = str(file_writer(take_last_posts()))
            for x in range(0, len(text), MESS_MAX_LENGHT):
                mess = text[x: x + MESS_MAX_LENGHT]
                bot.send_message(message.chat.id, mess)


# RUN
bot.polling(none_stop=True)
