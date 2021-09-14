from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

truthOrDare = KeyboardButton("Правда или действие")
iHaveNeverDone = KeyboardButton("Я никогда не...")

# markup3 = ReplyKeyboardMarkup().add(truthOrDare, iHaveNeverDone)

markup0 = ReplyKeyboardMarkup(resize_keyboard=True).row(
    truthOrDare, iHaveNeverDone
)

age0 = KeyboardButton("12+")
age1 = KeyboardButton("16+")
age2 = KeyboardButton("18+")
proger = KeyboardButton("Прогерам!")
back = KeyboardButton("Назад")

markup1 = ReplyKeyboardMarkup(resize_keyboard=True).add(age0, age1, age2, proger, back)