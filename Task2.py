#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10

list = [1, 2, 2, 1, 1, 3, 2, 5, 5]

def dup(x):
    duplicate = []
    unique = []
    for i in x:
        if i in unique:
            duplicate.append(i)
        else:
            unique.append(i)
    print("Дубликаты: ",duplicate)
    print("Уникальный список: ",unique)


dup(list)