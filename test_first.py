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


parametrizes_2 = [
    (1000, 1000, 12, 900, False),
    (1000, 3000, 12, 200, True),
]

@pytest.mark.parametrize('salary, how_much, mounths, cost_per_mounth, booltf', parametrizes_2)
def test_bank_count(salary, how_much, mounths, cost_per_mounth, booltf):
    res = bank_program.bank_count_2(salary, how_much, mounths, cost_per_mounth)
    assert res == booltf



# Тест будет пропускаться (помечатся как skip если провалиться и проходить как pass в случае выполнения).
@pytest.mark.xfail()
def test_xfail():
    res = sum([1,2,3])
    assert res == 6


# Тест будет пропускаться и отображаться как skipped.
@pytest.mark.skip()
def test_skip():
    res = sum([1, 2, 5])
    assert res == 6
