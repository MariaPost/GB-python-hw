# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open("my_file2.txt", "r") as f:
    lines = 0
    words = 0
    count = 0
    for line in f:
        lines += line.count("\n")
        words = line.count(" ") + 1
        count += 1
        print(f"В строке {count} слов: {words}")

print(f"Строк в файле: {lines}")
