""" 
Паттерн проектирования Memento (Хранитель) 

Не нарушая инкапсуляции, фиксирует и выносит за пределы объекта 
его внутреннее состояние так, чтобы позднее можно было 
восстановить в нем объект.
"""


class Memento:
    """ Хранитель """
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    """ Опекун """
    def __init__(self):
        self._memento = None
    
    def get_memento(self):
        return self._memento
    
    def set_memento(self, memento):
        self._memento = memento


class Originator:
    """ Создатель """
    def __init__(self):
        self._state = None
    
    def set_state(self, state):
        self._state = state
    
    def get_state(self):
        return self._state
    
    def save_state(self):
        return Memento(self._state)
    
    def restore_state(self, memento):
        self._state = memento.get_state()


if __name__ == '__main__':
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state('on')
    print(originator.get_state())
    caretaker.set_memento(originator.save_state())

    originator.set_state('off')
    print(originator.get_state())
    caretaker.set_memento(originator.save_state())

    originator.set_state('njn')

    originator.restore_state(caretaker.get_memento())
    originator.restore_state(caretaker.get_memento())

    print(originator.get_state())