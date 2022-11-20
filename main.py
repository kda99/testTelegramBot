import telebot

bot = telebot.TeleBot('5979217789:AAFUnZnT3-8zwOaKIMZXWb_2EaqN9s8Cwsk')
space = ''


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else space}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Посетить веб сайт', url='yandex.ru'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = telebot.types.KeyboardButton('Веб сайт')
    start = telebot.types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Классное фото!!!')


bot.polling(none_stop=True)
