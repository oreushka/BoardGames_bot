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
counter1 = 0
counter2 = 0

@dp.message_handler(commands=['start'])                                                                 # Hello
async def process_start_command(message: types.Message):
    await message.answer("Привет! Выбирай, в какую игру сыграем сегодня. Чтобы узнать правила, введи /help", reply_markup=kb.markup0)

@dp.message_handler(commands=['help'])                                                                  # Help
async def process_help_command(message: types.Message):
    await message.answer("Просто нажми на кнопку с нужной тебе игрой! \n "
                         "1. Правда или действие - выполни заданное действие или честно ответь на вопрос \n"
                         "2. Я никогда не - если кто-то из игроков делал хоть раз заданное действие, ему необходимо "
                         "об этом заявить: загнуть палец, выпить, хлопнуть, что угодно. Если с действием связана "
                         "интересная история, её можно всем рассказать \n"
                         "3. Alias - поделитесь на 2 команды. Командам по очереди будут даваться слова. Какая из команд"
                         " угадывает первой, той начисляются баллы", reply_markup=kb.markup0)

@dp.message_handler()                                                                                   # Send message
async def echo_message(message: types.Message):
    global game
    global step
    global counter1
    global counter2
    global duble

    if step == 0:
        if message.text == "Правда или действие":
            await message.answer("Я выбираю правду", reply_markup=kb.markup1)
            game = Game.TruthOrDare()
            step = 1
        elif message.text == "Я никогда не...":
            await message.answer("Я выбираю стыд!!!", reply_markup=kb.markup1)
            step = 1
            game = Game.I_never()
        elif message.text == "Alias":
            await message.answer("!!!Разделитесь на 2 команды, минимум по 2 человека в каждой!!! \n"
                                 "Слово на экране может прочесть только один участник команды."
                                 " Чтобы получить своё первое слово, нажмите кнопку ПРОПУСТИТЬ", reply_markup=kb.markup2)
            step = 2
            counter1 = 0
            counter2 = 0
            game = Game.Alias()
            duble = game.get_game()
        else:
            await message.answer("Котик, выбери игру из менюшки. Ну пожаааалуйста", reply_markup=kb.markup0)
        return

    if step == 1:
        if message.text in ["12+", "16+", "18+", "Прогерам!"]:
            await message.answer(random.choice(game.get_game()[message.text]))
        elif message.text == "Назад":
            await message.answer("Окееей, давай снова выбирать игру", reply_markup=kb.markup0)
            step = 0
        else:
            await message.answer("Котик, я тебя не понимаю, у меня лапки. Тыкай только по менюшке, пожалуйста",
                                 reply_markup=kb.markup1)

    if step == 2:

        if len(duble) == 0:
            await message.answer("Игра закончена", reply_markup=kb.markup0)
            step = 0
        elif message.text == "Команда 1":
            counter1 += 1
            word = random.choice(duble)
            duble.remove(word)
            await message.answer(word)
        elif message.text == "Команда 2":
            counter2 += 1
            word = random.choice(duble)
            duble.remove(word)
            await message.answer(word)
        elif message.text == "Пропустить":
            word = random.choice(duble)
            duble.remove(word)
            await message.answer(word)
        elif message.text == "Закончить игру":
            await message.answer("Как жаль, что вы наигрались. Надеюсь, вы весело порезвились", reply_markup=kb.markup0)
            step = 0
        await message.answer("Команда 1: " + str(counter1) + "\nКоманда 2: " + str(counter2))

                                                                                                        #run long-polling
if __name__ == '__main__':                                                                              #polling
    executor.start_polling(dp, skip_updates = True)
