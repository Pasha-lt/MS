import bank_program
import pytest


parametrizes = [
    (1000, 100, 8, True),
    (1000, 100, 4, True),
    (100, 10000, 40, False),
]


@pytest.mark.parametrize('salary, how_much, mounths, booltf', parametrizes)
def test_bank_count(salary, how_much, mounths, booltf):
    """Вариант с вынесением тестовых значений из декоратора."""
    res = bank_program.bank_count(salary, how_much, mounths)
    assert res == booltf


parametrizes_2 = [
    (1000, 1000, 12, 900, False),
    (1000, 3000, 12, 200, True),
]

@pytest.mark.parametrize('salary, how_much, mounths, cost_per_mounth, booltf', parametrizes_2)
def test_bank_count(salary, how_much, mounths, cost_per_mounth, booltf):
    """Вариант с вынесением тестовых значений из декоратора."""
    res = bank_program.bank_count_2(salary, how_much, mounths, cost_per_mounth)
    assert res == booltf



@pytest.mark.xfail()
def test_xfail():
    """Тест будет пропускаться (помечатся как skip если провалиться и проходить как pass в случае выполнения)."""
    res = sum([1,2,3])
    assert res == 6



@pytest.mark.skip('Причина тест сломан')
def test_skip():
    """Тест будет пропускаться и отображаться как skipped."""
    res = sum([1, 2, 5])
    assert res == 6


@pytest.mark.skipif((bank_program.minutes_now%2 == 0), reason='если сейчас нечетная минута мы запускаем этот тест', )
def test_skipif_odd():
    """Тест будет пропускаться если сейчас нечетная минута."""
    res = sum([2, 2, 3])
    assert res == 7


@pytest.mark.skipif((bank_program.minutes_now%2 == 1), reason='если сейчас четная минута мы запускаем этот тест', )
def test_skipif_even():
    """Тест будет пропускаться если сейчас четная минута."""
    res = sum([10, 2, 3])
    assert res == 15