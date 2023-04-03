"""
Задание №2
Файл содержит числа и буквы. Каждый записан в отдельной строке.
Нужно считать содержимое в список так, чтобы сначала шли числа по
возрастанию, а потом слова по возрастанию их длины.
"""

with open("example1.txt", "r") as f:
    list_ = f.readlines()
    list_digit = list()
    list_alpha = list()
    for i in list_:
        i = i.replace("\n", '')
        if i.isdigit():
            i = int(i)
            list_digit.append(i)
        elif i.isalpha():
            list_alpha.append(i)
    list_digit.sort()
    list_alpha.sort(key=len)
    list_ = list_digit + list_alpha
    print(list_)


"""
Задание №3
Создать текстовый файл, записать в него построчно данные, которые
вводит пользователь. Окончанием ввода пусть служит пустая строка.
"""

with open("new_file.txt", 'w') as f:
    str_ = " "
    while True:
        str_ = input("Введите строку ")
        if str_ != "":
            f.write(str_ + "\n")
        else:
            break


"""
Задание №4
В текстовом файле посчитать количество строк, а также для каждой
отдельной строки определить количество в ней символов.
"""

with open("new_file.txt", "r") as f:
    print(f"кол-во строк в файле - {len(f.readlines())}")
    f.seek(0, 0)
    for i in f.readlines():
        print(f"длинна строки {i} - {len(i) - 1}")

"""
Домашнее задание
Есть массив состоящий из слов и чисел, нужно записать в
файл сначала слова в порядке их длины, а после слов
цифры в порядке возрастания
"""

mass = [123, "ckj", 4, 6, 11, "слово", "hhfd"]

list_digit = list()
list_alpha = list()

for i in mass:
    if type(i) is int:
        list_digit.append(i)
    else:
        list_alpha.append(i)

list_digit.sort()
list_alpha.sort(key=len)

with open("file_txt.txt", "w") as f:
    for i in list_alpha:
        f.writelines(i + "\n")
    for i in list_digit:
        f.writelines(str(i) + "\n")
