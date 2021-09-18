# Напишите функцию которая будет принимать Три аргумента(Зарплата, сумма кредита и на сколько месяцев).
# и возвращает True если кредит выдать можно и False если нет.
# def bank():
#     pass

def bank_count(salary, how_much,mounths):
    how_much += how_much*(mounths/10) # увеличиваем тело кредита взависимости от того на сколько месяцев.
    print(how_much)
    living_wage_of_month = 600
    return salary - how_much/mounths >= living_wage_of_month

if __name__ == '__main__':
    assert bank_count(salary=1000, how_much=100, mounths=8) == True
    assert bank_count(salary=1000, how_much=100, mounths=4) == True
    assert bank_count(salary=1000, how_much=10000, mounths=40) == False