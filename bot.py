import config
import logging
import requests
import datetime
import random
from config import TOKEN, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from filters import IsAdminFilters

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.filters_factory.bind(IsAdminFilters)

@dp.message_handler(commands=["weather"])
async def start_command(message: types.Message):
    code_to_smile = {
      "Clear": "Ясно \U00002600",
      "Clouds": "Облачно \U00002601",
      "Rain": "Дождь \U00002614",
      "Drizzle": "Дождь \U00002614",
      "Thunderstorm": "Гроза \U000026A1",
      "Snow": "Снег \U0001F328",
      "Mist": "Туман \U0001F32B"
    }

    try:
      r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q=tomsk&appid={open_weather_token}&units=metric"
      )
      data = r.json()

      city = data["name"]
      cur_weather = data["main"]["temp"]

      weather_description = data["weather"][0]["main"]
      if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
      else:
        wd = "Лень в окно посмотреть!?"

      humidity = data["main"]["humidity"]
      pressure = data["main"]["pressure"]
      wind = data["wind"]["speed"]
      sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
      sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
      length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
        data["sys"]["sunrise"])

      await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                          f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                          f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                          f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                          )

    except:
      print("1")

@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
  print("JOINED")
  await message.delete()

@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def cmd_ban(message: types.Message):
  if not message.reply_to_message:
    await message.reply("Эта команда должна быть ответом на сообщение!")
    return
  await message.bot.delete_message(chat_id=config.GROUP_ID, message_id=message.message_id)
  await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)
  await message.reply_to_message.reply("Бан!!!")

@dp.message_handler()
async def filter_messages(message: types.Message):
  if "test" in message.text:
    await message.reply("Маты - плохо!")
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)