import sys
sys.path.insert(0, '..')


class ChangeLan:
    def __init__(self):
        pass

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'
        else:
            raise AttributeError
