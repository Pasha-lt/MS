import bank_program
import pytest

# Вариант с вынесением тестовых значений из декоратора.
parametrizes = [
    (1000, 100, 8, True),
    (1000, 100, 4, True),
    (100, 10000, 40, False),
]


@pytest.mark.parametrize('salary, how_much, mounths, booltf', parametrizes)
def test_bank_count(salary, how_much, mounths, booltf):
    res = bank_program.bank_count(salary, how_much, mounths)
    assert res == booltf

#
# assert bank_count(salary=1000, how_much=100, mounths=8) == True
# assert bank_count(salary=1000, how_much=100, mounths=4) == True
# assert bank_count(salary=1000, how_much=10000, mounths=40) == False
