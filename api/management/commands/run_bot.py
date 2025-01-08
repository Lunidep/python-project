import telebot
from api.gigachat import giga_chat_request

API_TOKEN = '7688662807:AAF8dCBOS7WO2pzWSyXt6Zl8ZR-3FZ0R8Go'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я помогу вам найти идеальное место для отдыха. Укажите ваши предпочтения.")

@bot.message_handler(func=lambda message: True)
def recommend_place(message):
    ans = giga_chat_request(message.text)
    bot.reply_to(message, ans)

bot.polling()