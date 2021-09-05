from aiogram import Bot, types, Dispatcher, executor

import config
import logging

#bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#log level
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])                                         #hello
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])                                          #help
async def process_help_command(message: types.Message):
    await message.answer("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()                                                           #send message
async def echo_message(message: types.Message):
    await message.answer(message.text)

#run long-polling
if __name__ == '__main__':                                                      #polling
    executor.start_polling(dp, skip_updates = True)
