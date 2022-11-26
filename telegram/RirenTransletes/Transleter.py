from config import RU_SIMBOLS, EN_SIMBOLS


class RuEnTranslater:
    def __init__(self, text: str):
        self.text = text
        self.ru_symbols = RU_SIMBOLS
        self.en_symbols = EN_SIMBOLS
        self._translete()

    def _translete(self):
        """Преобразует русский текст английской раскладкой"""
        self.current_text = str()
        for letter in self.text:
            for index, symbol in enumerate(self.en_symbols):
                if letter == symbol:
                    self.current_text += self.ru_symbols[index]

    def __str__(self) -> str:
        return self.current_text


str_ = 'Ghbdtn? vtyz pjden vfrcbv'
print(RuEnTranslater(str_))
