import pytest
from Homework_1 import Human, Queue
import random


class Test_Human:
    @pytest.fixture()
    def person(self):
        name = "Linar"
        age = random.randint(15, 45)
        human = Human(name, age)
        return human

    @pytest.fixture()
    def queue(self):
        return Queue()

    def test_need_human(self, person, queue):
        assert person.takeaqueae(queue) == person # Нужный ли это человек

    def test_age(self, person):
        assert person.age <= 30   # Человеку меньше 30-ти
