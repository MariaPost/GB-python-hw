# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, li):
        self.li = li

    def __str__ (self):
        return "\n".join("\t".join(map(str, row)) for row in self.li)

    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.li)):
            for j in range(len(self.li[0])):
                result[i][j] = self.li[i][j] + other.li[i][j]

        return "\n".join("\t".join(map(str, row)) for row in result)

matrix1 = Matrix([[1, 3, 2], [5, 1, 2], [2, 3, 1]])
matrix2 = Matrix([[2, 1, 3], [1, 4, 1], [3, 4, 2]])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)