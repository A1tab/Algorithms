# Наибольшая возрастающая подпоследовательность от последовательности а
# Сложность алгоритма O(nlogn)


def gis(a):
    n = len(a)
    inf = float ('inf')
    L = [-inf] + [inf] * (n + 1)
    for i in range(n):           # Куда вставить a[i]?
        left = 0
        right = n + 1
        while left + 1 < right:
            middle = (left + right) // 2
            if L[middle] < a[i]:
                left = middle
            else:
                right = middle
        L[right] = a[i]

    i = n + 1                   # Длина нвп это последний индекс L где лежит какое то число из а, до него нужно дойти
    while L[i] == inf:
        i -= 1
    
    L.remove((-inf))         # Чтобы получить саму нвп, нужно очистить L от inf
    while (inf) in L:
        L.remove(inf)
    return f'Нвп: {L} \nЕё длина: {i}'


print(gis([31, 21, 6, 1, 77, 104, 2.2, 15, 61, 30, 1, 1, 77, 80]))
