
import telebot

bot = telebot.TeleBot("6422319355:AAF73XZbfr0QipeeQlCtDnN4g60I_2BglZI")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет мир!!!")

bot.polling(none_stop=True) 
         
