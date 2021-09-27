def setup_function(func):
    print(f'\n{"*" * 30}\n Set up {func}\n{"*" * 30}')


def teardown_function(func):
    print(f'\n{"*" * 30}\n Teardown {func}\n{"*" * 30}')


def test_first_st():
    print(f'\n{"*" * 30}\n test_first_st\n{"*" * 30}')
    res = sum([1, 2, 3, 5])
    assert res == 11
    assert res + 1 == 12


def test_second_st():
    print(f'\n{"*" * 30}\n test_second_st\n{"*" * 30}')
    res = sum([0, 1, 0, 1])
    assert res == 2


'''
Вывод
******************************
 Set up <function test_first_st at 0x7effdf088840>
******************************
******************************
 test_first_st
******************************
******************************
 Teardown <function test_first_st at 0x7effdf088840>
******************************
******************************
 Set up <function test_second_st at 0x7effdf0888c8>
******************************
******************************
 test_second_st
******************************
******************************
 Teardown <function test_second_st at 0x7effdf0888c8>
******************************

'''