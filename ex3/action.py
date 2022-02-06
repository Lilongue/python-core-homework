class BaseAction:
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
        if (hasattr(self, "weak_anemy_name") and hasattr(other, "weak_anemy_name")):
            return True if other.name == self.weak_anemy_name else False


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    weak_anemy_name = 'Scissors'

    def __init__(self):
        super().__init__('Rock')



class PaperAction(BaseAction):
    weak_anemy_name = 'Rock'

    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    weak_anemy_name = 'Paper'
    
    def __init__(self):
        super().__init__('Scissors')
