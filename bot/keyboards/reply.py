from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from mixsins import GenerateMenuMixin


class ReplyGenerateMenu(GenerateMenuMixin):
    kb_class = ReplyKeyboardMarkup
    button_class = KeyboardButton


start_menu_dict = {
    'Добавить задачу': {},
    'Все задачи': {}

}

start_menu = ReplyGenerateMenu().generate_menu(start_menu_dict, resize_keyboard=True)
