from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

location_send = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свою локацию 🛰', request_location=True)
)

number_send = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
)

inline_btn_1 = InlineKeyboardButton('Орел', callback_data="orel")
inline_btn_2 = InlineKeyboardButton('Решка', callback_data="reshka")
coinkb = InlineKeyboardMarkup()
coinkb.row(inline_btn_1,inline_btn_2)