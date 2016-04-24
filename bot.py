import config
import telebot
import time

def listener(messages):
    for mes in messages:
        if mes.content_type == 'text':
            bot.send_message(mes.chat.id, mes.text)

if __name__ == '__main__':
    bot = telebot.TeleBot(config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)