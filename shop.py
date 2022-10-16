from functools import WRAPPER_UPDATES
import telebot
from telebot import types
bot = telebot.TeleBot('5358193371:AAE2iDTdPJ8zPo6PdUV_6BRXyKVsrONDAaI')

def web_app_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width = 1)
    web_app_shop= types.WebAppInfo("https://olezha01.github.io/telegramshop/")
    one_btn = types.KeyboardButton(text="Заказать", web_app = web_app_shop)
    keyboard.add(one_btn)
    return keyboard
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Привет, я бот для заказа товара", reply_markup=web_app_keyboard())

bot.polling(none_stop=True, interval=0)
