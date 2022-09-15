class GenerateMenuMixin:
    """
    mixin class for generate menu
    """
    kb_class = None
    button_class = None

    @classmethod
    def generate_menu(cls, buttons_dict: dict, **kw) -> list[kb_class]:
        """

        :param buttons_dict: contains button_name and keyword arguments to button class
        example:
            { 'button1': {'callback_data1': 'handle1'},
              'button2': {'callback_data2': 'handle2'},
              ...
              'buttonN': {'callback_dataN': 'handleN'},

        :param kw: keyword arguments for keyboard class
        :return: keyboard class
        """
        kb = cls.kb_class(kw)
        buttons = []
        for key, val in buttons_dict.items():
            assert isinstance(key, str), f'Error generate menu: {key} is not str in buttons_dict'
            assert isinstance(val, dict), f'Error generate menu: {val} is not dict in buttons_dict'
            buttons.append(cls.button_class(key, **val))
        kb.add(*buttons)
        return kb
