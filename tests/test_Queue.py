import random

import pytest

from Homework_1 import Human, Queue

queue = Queue()


class Test_Queue:
    @pytest.fixture()
    def person(self):
        name = "Marat"
        age = random.randint(15, 45)
        human = Human(name, age)
        queue.add_item(human)
        return human

    def test_contains(self, person):
        assert queue.contains(person) == person

    def test_remove(self):
        assert queue.remove() == queue.lenght
