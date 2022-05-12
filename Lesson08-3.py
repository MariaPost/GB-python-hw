class OnlyNumbersError:

    def __init__(self, *args):
        self.elements = []

    def onlyNumbers(self):
        while True:
            answer = input("Введите число или stop для завершения: ")
            try:
                element = int(answer)
                self.elements.append(element)

            except ValueError:
                if answer == "stop":
                    print(self.elements)
                    exit()
                else:
                    print("Вводите только числа")

num1 = OnlyNumbersError()
OnlyNumbersError.onlyNumbers(num1)
