from random import randint


class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def takeaqueae(self, que):
        return Queue.static_add_person(que, self)

    def __repr__(self):
        return self.name


class Queue:
    def __init__(self):
        self.list = []
        self.lenght = 0

    @staticmethod
    def static_add_person(que, human):
        return que.add_item(human)

    def add_item(self, human):
        self.list.append(human)
        self.lenght += 1
        return human

    def clear(self, ):
        self.list = []
        self.lenght = 0
        return self.lenght

    def contains(self, elem: Human):
        if elem in self.list:
            return elem
        else:
            return 'Такого элемента нет'

    def remove(self):
        if self.lenght == 0:
            raise ValueError('Список пуст!')
        else:
            del self.list[-1]
            self.lenght -= 1
        return self.lenght

    def rnd_insert(self, name ,age , gender):
        human = Human(name,age,gender)
        if len(self.list) == 0:
            self.add_item(human)
            return human
        else:
            self.list.insert(randint(1, len(self.list)), human)
            return human

