# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.
#
def my_func (a, b, c):
    li = [a, b, c]
    list_max = []

    res1 = max(li)
    list_max.append(res1)
    li.remove(res1)

    res2 = max(li)
    list_max.append(res2)
    print("Сумма наибольших двух чисел равна:", sum(list_max))

my_func(int(input("Введите число1: ")), int(input("Введите число2: ")), int(input("Введите число3: ")))
