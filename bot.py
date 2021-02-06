import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton("🎲 Получить")
    item2 = types.InlineKeyboardButton("🛂 Помощь")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Нажми на - *Получить*, и я тебе скину нужные данные.".format(message.from_user),
        parse_mode='Markdown', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Получить':
            line = random.choice(open('pass.txt', encoding="utf-8").readlines())
            bot.send_message(message.chat.id, text=f'''<b>ФИО - Др - Серия и номер - ИНН</b>\n<code>{line}</code>''', 
                parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, 'Если есть вопросы то напишите @leelter')

# RUN
bot.polling(none_stop=True)