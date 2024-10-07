import telebot
import datetime
import time
import threading

bot = telebot.TeleBot("тут должен быть ваш апи")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет!!!  Напиши за что ты благодарен сегодня!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

def send_reminders(chat_id):
    first_time = "06:43"
    second_time = "14:00"
    end_time = "19:08"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_time or now == second_time or now == end_time:
            bot.send_message(chat_id, "Напоминание - сделай запись за что ты благодарен сегодня")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)