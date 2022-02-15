class BaseAction:
    WEAK_ENEMY_NAME = "no"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        # Проверять тип other не стал, но тут нужно бы
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __gt__(self, other):
        return True if other.name == self.WEAK_ENEMY_NAME else False


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    WEAK_ENEMY_NAME = 'Scissors'

    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    WEAK_ENEMY_NAME = 'Rock'

    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    WEAK_ENEMY_NAME = 'Paper'

    def __init__(self):
        super().__init__('Scissors')
