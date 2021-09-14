from aiogram import Bot, types, Dispatcher, executor

import config
import logging
import keyboard as kb

#bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#log level
logging.basicConfig(level=logging.INFO)


# Game
class Game():
    def get_game(self):
        return dict([("12+", 0), ("16+", 1), ("18+", 2), ("Прогерам!", 3)])

# Правда или действие
class TruthOrDare():
    def get_game(self):
        return dict([("12+", 10), ("16+", 11), ("18+", 12), ("Прогерам!", 13)])

# Я никогда не
class I_never():
    def get_game(self):
        return dict([("12+", 20), ("16+", 21), ("18+", 22), ("Прогерам!", 23)])

game = Game()
step = 0


@dp.message_handler(commands=['start'])                                         #hello
async def process_start_command(message: types.Message):
    await message.reply("Привет! Выбирай, в какую игру сыграем сегодня", reply_markup=kb.markup0)

@dp.message_handler(commands=['help'])                                          #help
async def process_help_command(message: types.Message):
    await message.answer("Просто нажми на кнопку с нужной тебе игрой!", reply_markup=kb.markup0)

@dp.message_handler()                                                           #send message
async def echo_message(message: types.Message):
    global game
    global step

    if step == 0:
        if message.text == "Правда или действие":
            await message.answer("Я выбираю правду", reply_markup=kb.markup1)
            game = TruthOrDare()
            step = 1
        elif message.text == "Я никогда не...":
            await message.answer("Я выбираю стыд!!!", reply_markup=kb.markup1)
            step = 1
            game = I_never()
        else:
            await message.answer("Котик, ну выбери игру из менюшки. Ну пожаааалуйста", reply_markup=kb.markup0)
        return

    if step == 1:
        if message.text in ["12+", "16+", "18+", "Прогерам!"]:
            await message.answer(game.get_game()[message.text])
        elif message.text == "Назад":
            await message.answer("Окееей, давай снова выбирать игру", reply_markup=kb.markup0)
            step = 0
        else:
            await message.answer("Котик, я тебя не понимаю, у меня лапки. Тыкай только по менюшке, пожалуйста", reply_markup=kb.markup1)


#run long-polling
if __name__ == '__main__':                                                      #polling
    executor.start_polling(dp, skip_updates = True)
