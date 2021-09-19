# Напишите функцию которая будет принимать Три аргумента(Зарплата, сумма кредита и на сколько месяцев).
# и возвращает True если кредит выдать можно и False если нет.
# def bank_count():
#     pass

def bank_count(salary, how_much,mounths):
    how_much += how_much*(mounths/10) # увеличиваем тело кредита взависимости от того на сколько месяцев.
    living_wage_of_month = 600
    return salary - how_much/mounths >= living_wage_of_month


# Усовершенствуйте предведущую функцию чтобы она принимала 4 аргумент затраты в месяц и
# исходя из этого расчитывала можем ли мы выдать кредит человеку.
# и возвращает True если кредит выдать можно и False если нет.
# bank_count_2():
#     pass
def bank_count_2(salary, how_much, mounths, cost_per_mounth):
    how_much += how_much*(mounths/10) # увеличиваем тело кредита взависимости от того на сколько месяцев.
    print(how_much)
    return salary - how_much/mounths >= cost_per_mounth


print(bank_count_2(salary=1000, how_much=1000, mounths=12, cost_per_mounth=200))

if __name__ == '__main__':
    assert bank_count(salary=1000, how_much=100, mounths=8) == True
    assert bank_count(salary=1000, how_much=100, mounths=4) == True
    assert bank_count(salary=1000, how_much=10000, mounths=40) == False
    assert bank_count_2(salary=1000, how_much=1000, mounths=12, cost_per_mounth=900) == False
    assert bank_count_2(salary=1000, how_much=3000, mounths=12, cost_per_mounth=200) == True