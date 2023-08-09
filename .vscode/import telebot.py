import telebot
from telebot import types
token='6422319355: AAF73XZbfr0QipeeQlCtDnN4g60I_2BglZI'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
	    bot.send_message(message.chat.id,'Привет')
