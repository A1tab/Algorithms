# Гномья сортировка
# Квадратичныq алгоритм сортировки (от N-1 итераций до N**2)

def gnome_sort(a):
    n = len(a)
    remember_index = 1                                                     # Запоминаем индекс от которого пошли назад, чтобы потом к нему вернуться
    k = 0
    while k < n-1:
        if a[k] <= a[k+1]:
            k, remember_index = remember_index, remember_index + 1
        else:
            a[k], a[k+1] = a[k+1], a[k]
            k -= 1
            if k < 0:                                                      # Проверка что не выходим за границу массива 
                k, remember_index = remember_index, remember_index + 1
    return a