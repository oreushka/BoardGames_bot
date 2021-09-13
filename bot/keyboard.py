from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

truthOrDare = KeyboardButton("Правда или действие")
iHaveNeverDone = KeyboardButton("Я никогда не...")

#markup3 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup(resize_keyboard=True).row(
    truthOrDare, iHaveNeverDone
)
