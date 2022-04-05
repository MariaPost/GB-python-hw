# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например, название. Тогда значение — список
# значений-характеристик, например, список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


products = []
results = {"название товара": [], "цена товара": [], "количество товара": [], "единица измерения товара": []}
while True:
        answer = int(input("Хотите добавить новый товар? Да -1, Нет - 0: "))
        if answer == 1:
            code = int(input("Введите код товара: "))

            caracteristics = {}

            name = input("Введите название товара: ")
            price = int(input("Введите цену товара: "))
            number = int(input("Введите количество товара: "))
            unit = input("Введите единицу измерения товара: ")


            caracteristics["название товара"] = name
            caracteristics["цена товара"] = price
            caracteristics["количество товара"] = number
            caracteristics["единица измерения товара"] = unit

            products.append(tuple([code, caracteristics]))
            results["название товара"].append(name)
            results["цена товара"].append(price)
            results["количество товара"].append(number)
            results["единица измерения товара"].append(unit)

        elif answer == 0:
            break
        else:
            answer = int(input("Хотите добавить новый товар? Да -1, Нет - 0: "))

print(products)
print(results)