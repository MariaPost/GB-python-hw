# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
rus_file = []

with open("my_file4.txt", "r") as f:

    for line in f:
        el = line.split("-")

        if el[0] in dic:
            rus_file.append(dic[el[0]] + "-" + el[1])

print(rus_file)

with open("my_file5.txt", "w", encoding="utf-8") as f:
    f.writelines(rus_file)
