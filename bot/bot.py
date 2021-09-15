from aiogram import Bot, types, Dispatcher, executor

import config
import logging
import random
import keyboard as kb
import Game

bot = Bot(token=config.TOKEN)                                                                           # bot init
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)                                                                 # log level

game = Game.Game
step = 0

@dp.message_handler(commands=['start'])                                                                 # Hello
async def process_start_command(message: types.Message):
    await message.answer("Привет! Выбирай, в какую игру сыграем сегодня", reply_markup=kb.markup0)

@dp.message_handler(commands=['help'])                                                                  # Help
async def process_help_command(message: types.Message):
    await message.answer("Просто нажми на кнопку с нужной тебе игрой!", reply_markup=kb.markup0)

@dp.message_handler()                                                                                   # Send message
async def echo_message(message: types.Message):
    global game
    global step

    if step == 0:
        if message.text == "Правда или действие":
            await message.answer("Я выбираю правду", reply_markup=kb.markup1)
            game = Game.TruthOrDare()
            step = 1
        elif message.text == "Я никогда не...":
            await message.answer("Я выбираю стыд!!!", reply_markup=kb.markup1)
            step = 1
            game = Game.I_never()
        else:
            await message.answer("Котик, ну выбери игру из менюшки. Ну пожаааалуйста", reply_markup=kb.markup0)
        return

    if step == 1:
        if message.text in ["12+", "16+", "18+", "Прогерам!"]:
            await message.answer(random.choice(game.get_game()[message.text]))
        elif message.text == "Назад":
            await message.answer("Окееей, давай снова выбирать игру", reply_markup=kb.markup0)
            step = 0
        else:
            await message.answer("Котик, я тебя не понимаю, у меня лапки. Тыкай только по менюшке, пожалуйста", reply_markup=kb.markup1)

                                                                                                        #run long-polling
if __name__ == '__main__':                                                                              #polling
    executor.start_polling(dp, skip_updates = True)
