import random

import pytest

from Homework_1 import Human, Queue

queue = Queue()


class Test_Queue:
    @pytest.fixture()
    def create_human(self):
        name = "Marat"
        age = random.randint(15, 45)
        human = Human(name, age)
        queue.add_item(human)
        return human

    def test_contains(self, create_human):
        assert queue.contains(create_human) == create_human

    def test_remove(self, create_human):
        assert queue.remove() == queue.lenght
