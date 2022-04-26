
# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def get_sum_fabrics(self):
        sum_fabrics = (self.size / 6.5 + 0.5) + (2 * self.height + 0.3)
        return (f'Общий расход ткани на пальто и костюм: {sum_fabrics}')

class Coat(Clothes):
    def __init__(self, size, height):
        Clothes.__init__(self, size, height)

    def coat_fabrics(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, size, height):
        Clothes.__init__(self, size, height)

    def suit_fabrics(self):
        return 2 * self.height + 0.3


clothes2 = Clothes(38, 1.8)
print(clothes2.get_sum_fabrics)
coat1 = Coat(38, 1.8)
print(coat1.coat_fabrics())
suit1 = Suit(38, 1.8)
print(suit1.suit_fabrics())
