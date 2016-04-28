import config
import telebot
import exchange_rates as rt
import weather as wth

bot = telebot.TeleBot(config.token)


def command_split(string):
    return string.split()


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    str = "Приветствую, Вас, хозяин!" + "\n" \
          + "Я умею выполнять такие команды: " + "\n" \
          + "/rates - курс валют" + "\n" \
          + "Параметры для /rates: " + "\n" \
          + "USD - доллар США" + "\n" \
          + "EUR - евро" + "\n" \
          + "RUR - рубль" + "\n" \
          + "/weather_current - текущая погода" + "\n" \
          + "/help - справка"
    bot.send_message(message.chat.id, str)


@bot.message_handler(commands=['rates'])
def handle_rates(message):
    if len(command_split(message.text)) > 1:
        bot.send_message(message.chat.id, rt.get_rates(command_split(message.text)[1]))
    else:
        bot.send_message(message.chat.id, rt.get_rates("USD"))
        bot.send_message(message.chat.id, rt.get_rates("EUR"))
        bot.send_message(message.chat.id, rt.get_rates("RUR"))


@bot.message_handler(commands=['weather_current'])
def handle_current_weather(message):
    bot.send_message(message.chat.id, wth.get_current_weather())


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
