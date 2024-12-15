import telebot
from config import token
from programmer import pro_skill

bot = telebot.TeleBot(token)
can = '/skill - покажет какой ты программист'
@bot.message_handler(commands=['skill'])
def send_bye(message):
    skillz = pro_skill(1)
    bot.reply_to(message, f"Ты программист на {skillz}")

@bot.message_handler(commands=['start'])
def send_bye(message):
    bot.reply_to(message, F'Вот что я могу: {can}')

bot.polling()