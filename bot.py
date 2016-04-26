import config
import telebot
import exchange_rates


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    str = "Здравствуйте, хозяин!" + "\n" + "Я умею выполнять такие команды: " + "\n" + "/rates - курс валют" + "\n"
    bot.send_message(message.chat.id, str)


@bot.message_handler(commands=['rates'])
def handle_rates(message):
    rates = list()
    rates = exchange_rates.get_rates()
    for item in rates:
        str1 = 'Валюта: ' + item['ccy'] + "\n"
        str2 = 'Покупка: ' + item['buy'] + " грн" + "\n"
        str3 = 'Продажа: ' + item['sale'] + " грн" + "\n"
        bot.send_message(message.chat.id, str1 + " " + str2 + " " + str3)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
