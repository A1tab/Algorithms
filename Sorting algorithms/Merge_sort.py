# Сортировка слиянием. Общий вид.
# Рекурентная сортировка  O(n*log*n)

def merge(a, b):
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:                  # Устойчивость. Сортировка называется устойчивой, если она не меняет порядок равных элементов (<=)
            c[n] = a[i]; i += 1; n += 1
        else:
            c[n] = b[k]; k += 1; n += 1
    while i < len(a):
        c[n] = a[i]; i += 1; n += 1
    while k < len(b):
        c[n] = b[k]; k += 1; n += 1
    return c

def merge_sort(a):
    if len(a) <= 1:
        return a
    middle = len(a) // 2
    left = a[:middle]                                   # Можно сделать срез списка как в этой строке
    right = [a[i] for i in range(middle, len(a))]       # или как в этой строке
    merge_sort(left)
    merge_sort(right)
    # print(left, right)
    c = merge(left, right)
    # print('1',a)
    for i in range(len(a)):                        # Чтобы отсортированные кусочки переписывались в правильном порядке
        a[i] = c[i]
    # print('2',a)
    return c # или "а" не важно


a = [6,1,27,3,2,8]
print(merge_sort(a))



# Сортировка слиянием. Нормальный вид.
def merge_two_lists(a, b):
    c = []
    i = k = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[k])
            k += 1
    if i < len(a):
        c += a[i:]                          # Добавить оставшуюся часть (уже отсортированного) списка, потому что списки а и b не равной длины
    if k < len(a):
        c += b[k:]                          # Oдна из этих строчек добавит None, поэтому проверки не нужны, мб только сэкономить время на + None
    return c

def merge_sort_2(a):
    if len(a) == 1:
        return a
    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    return merge_two_lists(left, right)


a = [6,1,27,3,21,22,22,22,6,3,2,8]

print(merge_sort_2(a))



#_________________________

# from Speed_test import *

# speed_test_compare(merge_sort, merge_sort_2, 10, a)
#merge_sort_2 быстрее на ~0.0000004 секунд


# speed_test_sort(merge_sort_2)

#0.0095127  Слияние
#0.0043608
#0.0078494

#0.000428   Гномы
#0.000254 
#0.000060

#0.076913   Методом выбора
#0.339076
#0.008233



#_____________________________________

# from Hoar_sort import *

# speed_test_compare(hoar_sort, merge_sort_2, 100, a)

# разницы у рекурсивных сортировок практически нет. merge_sort_2 на 0.0000965 секунды быстрее




