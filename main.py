import telebot
from telebot import types

from config import API_TOKEN
from questions_list import get_questions_list

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def first_step(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.',
                     reply_markup=call_menu_buttons())


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
                     'Функционал бота 🤖:\n/start  👉 Запуск бота\n'
                     '/generate  👉 Сгенерировать 5 вопросов из собеседований')


@bot.message_handler(commands=['generate'])
def get_questions(message):
    bot.send_message(message.chat.id, get_questions_list())


@bot.message_handler()
def custom_first_step(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.',
                         reply_markup=call_menu_buttons())


def call_menu_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/generate')
    btn2 = types.KeyboardButton('/github')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('/help')
    btn4 = types.KeyboardButton('/site')
    markup.row(btn3, btn4)
    return markup


bot.infinity_polling()
