

# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self, asph_mass, asph_thickness):
        self.asph_mass = asph_mass
        self.asph_thickness = asph_thickness
        volume_mass = self._length * self._width * self.asph_mass * self.asph_thickness/1000
        print(volume_mass)

road1 = Road(20, 5000)

road1.mass(25, 5)

