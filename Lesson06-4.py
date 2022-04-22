# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = is_police

    def go(self):
        print(f"Автомобиль {self.name} едет")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        print(f'Автомобиль {self.name} поворачивает {direction}')

    def show_speed(self):
        print(f'Автомобиль {self.name} едет со скоростью {self.speed} км/ч')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 60:
            print(f"Вы двигаетесь с допустимой в городе скоростью {self.speed} км/ч.")
        else:
            print(f"Вы двигаетесь со скоростью {self.speed} км/ч. Вы превышаете допустимую в городе скорость 60км/ч.")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 40:
            print(f"Вы двигаетесь с допустимой в городе скоростью {self.speed} км/ч.")
        else:
            print(f"Вы двигаетесь со скоростью {self.speed} км/ч. Вы превышаете допустимую в городе скорость 40км/ч.")

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


car1 = TownCar(65, "green", "Honda", False)
car2 = SportCar(140, "red", "Ferrari", False)
car3 = WorkCar(35, "white", "Ford", False)
car4 = PoliceCar(80, "black", "BMW", True)

print(car1.name)
print(car2.speed)

car1.go()
car3.stop()
car2.show_speed()
car4.turn("налево")

car1.show_speed()
car3.show_speed()
