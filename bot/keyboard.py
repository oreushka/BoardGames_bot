from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButtonPollType

truthOrDare = KeyboardButton("Правда или действие")
iHaveNeverDone = KeyboardButton("Я никогда не...")
alias = KeyboardButton("Alias")

markup0 = ReplyKeyboardMarkup(resize_keyboard=True).row(
    truthOrDare, iHaveNeverDone, alias
)

age0 = KeyboardButton("12+")
age1 = KeyboardButton("16+")
age2 = KeyboardButton("18+")
proger = KeyboardButton("Прогерам!")
back = KeyboardButton("Назад")

markup1 = ReplyKeyboardMarkup(resize_keyboard=True).add(age0, age1, age2, proger, back)

team1 = KeyboardButton("Команда 1")
team2 = KeyboardButton("Команда 2")
skip = KeyboardButton("Пропустить")
end = KeyboardButton("Закончить игру")

markup2 = ReplyKeyboardMarkup(resize_keyboard=True).add(team1, team2, skip, end)


