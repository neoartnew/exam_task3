

class Tomato:
    states = {'Семечка': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        return False



class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник начал работу...')
        self._plant.grow_all()
        print('Садовник закончил работу.')

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран')
            self._plant.give_away_all()
        else:
            print('Томаты еще не дозрели')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу в росте')
        print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней')

# Тесты:
# 1. Вызовите справку по садоводству
Gardener.knowledge_base()

# 2. Создайте объекты классов TomatoBush и Gardener
bush = TomatoBush(3)
gardener = Gardener('Artem', bush)

# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
gardener.work()
gardener.work()
gardener.work()

# 4. Попробуйте собрать урожай
gardener.harvest()

# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

# 6. Соберите урожай
gardener.work()
gardener.harvest()