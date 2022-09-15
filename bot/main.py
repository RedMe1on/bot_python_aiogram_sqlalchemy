from aiogram import Bot, Dispatcher, types, executor

bot = Bot('638951866:AAHdYDvSutD3Op-kRBZ8phWiEIDLIVZSVxg', parse_mode="HTML")

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer(
        "Ну здарова, Отец!\n\n"
        "Хочешь работы подкинуть? Жми /add_task или напиши Добавь\n"
        "Рандомную задачку выкинуть: /roulette или напиши Рулетка\n"
        "Все показать \U0001F60F: /all_tasks или напиши Все или Список\n"
        "Задачи на сегодня: /today_tasks или напиши Сегодня\n"
        "Задачи на завтра: /tomorrow_tasks или напиши Завтра\n"
        "Задачи на неделю: /week_tasks или напиши Неделя\n"
        "Просроченные задачи (самая частая кнопка - 100%): /overdue_tasks или напиши Просроченные\n"
        "Задачи без даты: /without_deadline или напиши Без даты или Без срока\n"
        "Изменить настройки бота: /settings или напиши Настройки или Настройка\n"
        "Нужна помощь по боту? Жми /help или напиши Помогите или Хелп, или Помощь\n")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)