import pytest


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Task:
    def __init__(self, name):
        self.name = name


@pytest.fixture
def user_1():
    return User(name='Andrey', age=30)

@pytest.fixture
def tast_1(user_1):
    """В фикстуре как бы наследуемся от другой фиктуры"""
    return Task(name=user_1.name)

def test_task(user_1, tast_1):
    assert tast_1.name == user_1.name