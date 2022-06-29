from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Settings menu
switch_on_switch_off_send_today_task = InlineKeyboardButton('Вкл/Выкл регулярную отправку задач',
                                                            callback_data='switch_on_switch_off_send_today_tasks_in_the_morning')
switch_on_switch_off_send_stoicism_quotes = InlineKeyboardButton('Вкл/Выкл регулярную отправку фраз стоицизма',
                                                            callback_data='switch_on_switch_off_send_stoicism_quotes_in_the_morning')
switch_on_switch_off_send_compliments_and_quotes = InlineKeyboardButton('Вкл/Выкл отправку комплиментов и цитат',
                                                                        callback_data='switch_on_switch_off_send_compliments_and_quotes')
set_morning_time = InlineKeyboardButton('Установить утреннее время', callback_data='set_morning_time')
settings_menu = InlineKeyboardMarkup().add(switch_on_switch_off_send_today_task).add(
    switch_on_switch_off_send_today_task).add(
    switch_on_switch_off_send_compliments_and_quotes).add(set_morning_time)
