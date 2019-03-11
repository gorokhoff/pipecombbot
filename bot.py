import telebot
import parser
TOKEN = ""
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    global isRunning
    if not isRunning:
        chat_id = message.chat.id
#        text = message.text
#        msg = bot.send_message(chat_id, 'Сколько вам лет?')
        isRunning = True    

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - парсер хабра.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    elif text == "bip":
        bot.send_message(chat_id, 'bop')
	else:
        bot.send_message(chat_id, 'Простите, я вам не понял :(')
bot.polling()
