import telebot
import time
from multiprocessing.context import Process
import schedule
import datetime
import threading
import shelve

from bd import users_db # Импортируем базу данных
from telebot import types
from threading import Thread, Lock

APP_NAME='nickivixbot'
bot = telebot.TeleBot('1203796579:AAEhYHUDIHTeuk2H7HVylLPjzequFhssLHM')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Оповещать про урок', 'Расписание')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты запустил меня', reply_markup=keyboard1)
    if not users_db.find_one({"chat_id": message.chat.id}):
        users_db.insert_one({"chat_id" : message.chat.id})
    else:
        bot.send_message(message.chat.id, 'Привет, ты запустил меня снова')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'оповещать про урок':
        bot.send_message(message.chat.id, 'Я буду присылать тебе урок и ссылку на него за 5 минут до его начала')
    elif message.text.lower() == 'расписание':
        bot.send_photo(message.chat.id, open('rasp.jpg', 'rb')) 
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить')

def send_message_to_all_users():
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], 'https://kr4u4ba.xyz Есть расписание, дз, и многое другое.')
            except Exception as e:
                print('Something wrong')
def send_message_to_all_users1():
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], 'История: ' + 'без ссылки')
            except Exception as e:
                print('Something wrong')
def send_message_to_all_users2():
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], 'Математика: '+ 'https://bit.ly/3bfAO28')
            except Exception as e:
                print('Something wrong')
def send_message_to_all_users3():
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], 'Английский: '+ 'https://meet.lync.com/dlitdp-dlit/virolajnen_n/B2JG2N9G')
            except Exception as e:
                print('Something wrong')
def send_message_to_all_users4():
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], 'Астрономия: '+ 'https://meet.lync.com/dlitdp-dlit/orlyansky/MT73Q14M')
            except Exception as e:
                print('Something wrong')
def send_message_to_all_users5():
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], 'Напиши /start ещё раз!')
            except Exception as e:
                print('Something wrong')
def send_message_to_all_users6():
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], 'Я самоуничтожаюсь на неопределённый срок, чтобы из-за меня никому не было плохо, хоть я и создан как дополнение')
            except Exception as e:
                print('Something wrong')

schedule.every().wednesday.at("08:55").do(send_message_to_all_users1)
schedule.every().wednesday.at("09:55").do(send_message_to_all_users2)
schedule.every().wednesday.at("10:55").do(send_message_to_all_users3)
schedule.every().wednesday.at("11:55").do(send_message_to_all_users4)
schedule.every().wednesday.at("10:15").do(send_message_to_all_users5)
schedule.every().wednesday.at("10:50").do(send_message_to_all_users6)

schedule.every().tuesday.at("22:15").do(send_message_to_all_users1)
schedule.every().tuesday.at("22:15").do(send_message_to_all_users2)
schedule.every().tuesday.at("22:15").do(send_message_to_all_users3)
schedule.every().tuesday.at("22:15").do(send_message_to_all_users4)
schedule.every().tuesday.at("22:15").do(send_message_to_all_users)

class ScheduleMessage():
	def try_send_schedule():
		while True:
			schedule.run_pending()
			time.sleep(1)

	def start_process():
		p1 = Process(target=ScheduleMessage.try_send_schedule, args=())
		p1.start()

if __name__=='__main__':
	ScheduleMessage.start_process()
	try:
		bot.polling(none_stop=True, interval=0)
	except:
		pass