class ComplexNumbers:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"z = {self.a} + {self.b} * i"

    def __add__(self, other):
        return f"z = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"z = {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b} * i"


z1 = ComplexNumbers(2, 1)
z2 = ComplexNumbers(3, 4)

print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
