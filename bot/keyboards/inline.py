from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from mixsins import GenerateMenuMixin


class InlineGenerateMenu(GenerateMenuMixin):
    kb_class = InlineKeyboardMarkup
    button_class = InlineKeyboardButton


setting_menu_dict = {
    'Вкл/Выкл регулярную отправку задач': {
        'callback_data': 'switch_on_switch_off_send_today_tasks_in_the_morning'
    },
    'Вкл/Выкл регулярную отправку фраз стоицизма': {
        'callback_data': 'switch_on_switch_off_send_stoicism_quotes_in_the_morning'
    }

}

settings_menu = InlineGenerateMenu.generate_menu(setting_menu_dict)

