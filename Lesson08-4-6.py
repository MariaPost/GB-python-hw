class OfficeEquipment:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.storage = []
        self.warehouse = []


    def movement(self, placename):
        self.storage.append(placename)


    def buy(self):
        while True:
            answer = int(input("Хотите добавить новую позицию? Да -1, Нет - 0: "))
            if answer == 1:
                try:
                    name = input("Введите название: ")
                    quantity = int(input("Введите количество товара: "))
                    price = int(input("Введите цену товара: "))
                    el = {"Название": name, "Количество": quantity, "Цена": price}
                    self.warehouse.append(el)
                    print(self.warehouse)
                except:
                    print("Данные введены неправильно")

            elif answer == 0:
                break
            else:
                answer = int(input("Хотите добавить новую позицию? Да -1, Нет - 0: "))



class Printer(OfficeEquipment):

    def __init__(self, name, quantity, price, printspeed):
        OfficeEquipment.__init__(self, name, quantity, price)
        self.printspeed = printspeed
        self.storage = []

    def __str__(self):
        return f'Название: {self.name}, Количество: {self.quantity}, Цена: {self.price}, Печать стр/мин: {self.printspeed}'



class Scaner(OfficeEquipment):

        def __init__(self, name, quantity, price, scanspeed):
            OfficeEquipment.__init__(self, name, quantity, price)
            self.scanspeed = scanspeed
            self.storage = []

        def __str__(self):
            return f'Название: {self.name}, Количество: {self.quantity}, Цена: {self.price}, Сканирование стр/мин: {self.scanspeed}'


class Xerox(OfficeEquipment):

        def __init__(self, name, quantity, price, xeroxspeed):
            OfficeEquipment.__init__(self, name, quantity, price)
            self.xeroxspeed = xeroxspeed
            self.storage = []

        def __str__(self):
            return f'Название: {self.name}, Количество: {self.quantity}, Цена: {self.price}, Копирование стр/мин: {self.xeroxspeed}'


elem1 = Printer("Canon", 3, 250, 20.2)
print(elem1)
elem2 = Scaner("Epson", 2, 450, 2)
print(elem2)
elem3 = Xerox("Xerox", 1, 650, 10.3)
print(elem3)

elem1.movement("Office1")
print(elem1.storage)
elem1.movement("Warehouse2")
print(elem1.storage)

print(OfficeEquipment.buy(elem1))
