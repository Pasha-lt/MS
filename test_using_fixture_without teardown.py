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


# ставим autouse=True фикстура отработает даже если она не будет вызвана. По дефолту False.
@pytest.fixture(scope='function', autouse=True)
def create_file():
    with open('1.txt', 'w') as f:
        f.write('12')


def test_user(user):
    '''В этот тест мы домешали фикстуру user'''
    user.new_title('King ')
    assert user.person_new_title == 'King Roman'
