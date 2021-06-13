from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

location_send = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свою локацию 🛰', request_location=True)
)

number_send = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
)