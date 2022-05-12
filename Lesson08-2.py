
class DivByZero:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    @staticmethod
    def new_division(obj):
        try:
            res = obj.number1 / obj.number2
            return res
        except ZeroDivisionError:
            print("На ноль делить нельзя!")

div1 = DivByZero(20, 2)
print(DivByZero.new_division(div1))

div2 = DivByZero(4, 0)
print(DivByZero.new_division(div2))
