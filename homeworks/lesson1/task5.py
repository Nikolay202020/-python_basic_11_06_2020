
'''
 5) Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки
 (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы и определите прибыль
 фирмы в расчете на одного сотрудника.
'''

while True:

    v = input("Введите выручку (руб)  -  ")

    if v.isdigit():
        break
    else:
        print('Ошибка ввода! Это не число!')
v = int(v)

while True:

    w = input("Введите издерки (руб)  -  ")

    if w.isdigit():

        break
    else:
        print('Ошибка ввода! Это не число!')

w = int(w)

if v > w:

    p = v - w
    print('Фирма отработала с прибылью (руб) - ' + str(p))
    r = str(p / v)
    print('Рентабельность выручки составила - ' + r)

    while True:

        u = input('Введите количество работников  -  ')
        if u.isdigit():
            break
        else:
            print('Ошибка ввода! Это не число!')

    u = int(u)
    p2 = str(p / u)
    print('Прибыль фирмы на одного сотрудника составила (руб) - ' + p2)

elif v == w:
    print("Фирма отработала без прибыли и без убытка")
else:
    p1 = str(w - v)
    print('Фирма отработала с убытком (руб) - ' + p1)