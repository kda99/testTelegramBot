import telebot

bot = telebot.TeleBot('5979217789:AAFUnZnT3-8zwOaKIMZXWb_2EaqN9s8Cwsk')
space = ''
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else space}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)