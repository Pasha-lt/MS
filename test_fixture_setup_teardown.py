import pytest


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Зовут {self.name}. прожил уже {self.age}'


@pytest.fixture
def user():
    obj = User(name='Roman', age=30) #setup
    yield obj # возвращает
    del obj # teardown


def test_23(user):
    assert str(user) == 'Зовут Roman. прожил уже 30'
