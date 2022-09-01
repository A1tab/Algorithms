# Сортировка подсчетом О(N)
def count_sort(a):
    n = len(a)
    f = [0] * n
    b = []
    for k in range(n):
        f[a[k]] += 1
    for q in range(len(f)):
        for i in range(f[q]):
            b.append(q)
    return b