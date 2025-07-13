from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Подписаться на рассылку"),
            KeyboardButton(text="Отписаться от рассылки")
        ],
        [
            KeyboardButton(text="Получить список бесплатных игр")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Выберите дейтсвие",
    selective=True,
)