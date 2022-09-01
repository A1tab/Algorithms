# Сортировка Тони Хоара (Quick sort). Общий вид (жрет много памяти)
# Рекурентная сортировка  O(n*log*n)

def hoar_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]              # Выбираем наугад барьерный элемент,  
    l, m, r = [],[],[]
    for x in a:                 # и расскладывам остальные по трем массивам, меньше барьерного, больше или равно
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
        hoar_sort(l)            # левый и правый массив нужно отсортировать, а в среднем все элементы одинаковые
        hoar_sort(r)
        k = 0
        print(l+m+r)
        for x in l + m + r:     # пробегаем по трем массивам как по одному
            a[k] = x
            k += 1              # ничего не возвращает, а изменяет данный ей массив



# Сортировка Тони Хоара (Quick sort). Крутой вид
def hoar_sort_2(a):
    if len(a) <= 1:
        return a
    barrier = a[0]
    l = list(filter(lambda x: x < barrier, a))
    m = [i for i in a if i == barrier]              # генератор списков добавляет в middle все элементы равные барьерному
    r = list(filter(lambda x: x > barrier, a))
    return hoar_sort_2(l) + m + hoar_sort_2(r)


a = [6,27,1,3,2,8]
print(hoar_sort(a))
print(hoar_sort_2(a))


#_________________________________________________

# from Speed_test import *

# speed_test_compare(hoar_sort, hoar_sort_2, 100, random_list)

# # В плане скорости разницы нет. Первая реализация быстрее на 0.0002146 секунды


