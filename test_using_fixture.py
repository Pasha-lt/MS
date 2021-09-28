import pytest


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def new_title(self, title):
        self.person_new_title = title + self.name

@pytest.fixture(scope='function')
def user():
    my_fixture = User(name='Roman', age=30)
    return my_fixture


def test_user(user):
    '''В этот тест мы домешали фикстуру user'''
    user.new_title('King ')
    assert user.person_new_title == 'King Roman'
    