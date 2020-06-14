"HOME WORK"
"""
1)Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
 проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
  Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
n = bin(16)
n1 = oct(16)
n2 = hex(16)
n3 = complex(5, 6)
n4 = list('Hello 37')
n5 = tuple('start 73')
n6 = set('second 120')
n7 = frozenset('88 hp')
n8 = {"A1": "123", "A2": "False"}
n9 = bytes(b'bytes')
n10 = bytearray(b'hello Teacher!')

l1 = [3, 122, 2.55, n, n1, n2, n3, 'World', n4, n5, n6, n7, n8, n9, n10, True, False, None]
for el in l1:

    print(el)

    print(type(el))
"""
 2) Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
 элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
 сохранить на своем месте. Для заполнения списка элементов необходимо использовать
 функцию input() .
"""

a = list(input('Введите данные:\n'))

print(' '.join([str(i) for i in a]))# для удобства контроля.

for i in range(1, len(a), 2):

      a[i], a[i - 1] = a[i - 1], a[i]

print(' '.join([str(i) for i in a]))



"""
 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
  Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
   Напишите решения через list и через dict.
"""
n_month = list(input('Введите номер месяца:\n'))

"""""
 4) Пользователь вводит строку из нескольких слов, разделённых пробелами. 
 Вывести каждоe слово с новой строки. Строки необходимо пронумеровать. 
 Если в слово длинное, выводит только первые 10 букв в слове.
"""""

"""""
 5) Реализовать структуру « Рейтинг » , представляющую собой не возрастающий набор
 натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
 в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
 значением должен разместиться после них.
 Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
 Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3 , 2.
 © geekbrains.ru 37
 Пользователь ввел число 8. Результат: 8 , 7, 5, 3, 3, 2.
 Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1 .
 Набор натуральных чисел можно задать непосредственно в коде, 
 например, my_list = [7, 5, 3, 3, 2].
"""""

'''''
 6) *Реализовать структуру данных « Товары » . Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
 элемента — номер товара и словарь с параметрами (характеристиками товара: название,
 цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
 запрашивать все данные у пользователя.
 Пример готовой структуры:
 [
 (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
 (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
 (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
 ]
 Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
 характеристика товара, например название, а значение — список значений-характеристик,
 например список названий товаров.
 Пример:
 {
 “название”: [“компьютер”, “принтер”, “сканер”],
 “цена”: [20000, 6000, 2000],
 “количество”: [5, 2, 7],
 “ед”: [“шт.”]
'''''