# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

info_li = []
while True:
    info = input("Введите данные: ")
    if info == " ":
        break
    else:
         file_info = info + "\n"
         info_li.append(file_info)

with open("my_file1.txt", "w") as f:
    f.writelines(info_li)
