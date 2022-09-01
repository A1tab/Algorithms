# Бинарный поиск в (отсортированном) массиве. Задача состоит в том чтобы найти индексы границ вхождения элемента num в списке а 


def bin_search(a, num):
    left = -1                           # -1  0  1  2  3  4  5  len(a)
    right = len(a)                      #    [1, 3, 3, 6, 7, 9]
    while right - left > 1:
        middle = (left + right) // 2    # берем элемент по середине
        if a[middle] < num:             # если значение там меньше искомого числа,
            left = middle               # то отбрасываем все что левее этой середины
        else:
            right = middle              # а если больше, то отбрасываем то что правее
    left_bound = left                   # так находим сначала левую границу
    
    left = -1                           # перед тем как искать правую, границы нужно сбросить
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] <= num:
            left = middle
        else:
            right = middle
    right_bound = right

    if right_bound - left_bound == 1:   # если правый индекс минус левый = 1, значит между ними нет никаких элементов
        return "Такого элемента нет"
    else:
        return left_bound, right_bound  # Скорость бинарного поиска очень высока - она пропорциональна логарифму от колва элементов = O(log₂N)


a = [1,2,2,2,3,3,5,5,5,5,5,7,8,8,8,9,9,9,9,9,12]
print(bin_search(a,5))
print(bin_search(a,1))
print(bin_search(a,12))
print(bin_search(a,-2))
print(bin_search(a,200))





