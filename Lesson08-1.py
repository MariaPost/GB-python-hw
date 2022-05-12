
class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        print(f"{self.day} / {self.month} / {self.year}")

    @classmethod
    def createdate(cls, date):
        day, month, year = date.split("/")
        return cls(day, month, year)

    @staticmethod

    def validation(obj):

        if int(obj.day) < 1 or int(obj.day) > 31:
            print("Введен неправильный день")
        if int(obj.month) < 1 or int(obj.month) > 12:
            print("Введен неправильный месяц")
        if int(obj.year) < 1900:
            print("Введен неправильный год")
        else:
            print("Дата введена правильно")
            print((f"{obj.day} / {obj.month} / {obj.year}"))


date1 = "01/02/2022"
data1 = Data.createdate(date1)
Data.validation(data1)

date2 = "01/15/1896"
data2 = Data.createdate(date2)
Data.validation(data2)
