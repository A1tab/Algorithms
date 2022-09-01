import time
from Insertion_sort import *
from Bubble_sort import *
from Gnome_sorting import *
from Selection_sort import *
from Count_sort import *
from Speed_test import *


def speed_champ():
    q,w,e,r,t,y = 0,0,0,0,0,0
    for i in range(10):                                                # Сюда вбить число раундов
        a = b = c = d = f = list_generator(maxrange=7000)
        print('Длина массива: ',len(a))

        tic = time.perf_counter()
        insert_sort(a)
        tac = time.perf_counter()
        tmp1 = tac - tic
        print(f"Вычисление Вставок   заняло {tac - tic:0.6f} секунд")

        tic = time.perf_counter()
        choice_sort(b)
        tac = time.perf_counter()
        tmp2 = tac - tic
        print(f"Вычисление Выбора    заняло {tac - tic:0.6f} секунд")

        tic = time.perf_counter()
        bubble_sort(c)
        tac = time.perf_counter()
        tmp3 = tac - tic
        print(f"Вычисление Пузырька  заняло {tac - tic:0.6f} секунд")

        tic = time.perf_counter()
        gnome_sort(d)
        tac = time.perf_counter()
        tmp4 = tac - tic
        print(f"Вычисление Гномов    заняло {tac - tic:0.6f} секунд")

        tic = time.perf_counter()
        count_sort(f)
        tac = time.perf_counter()
        tmp5 = tac - tic 
        print(f"Вычисление Подсчетом заняло {tac - tic:0.6f} секунд")

        if tmp1 < tmp2 and tmp1 < tmp3 and tmp1 < tmp4 and tmp1 < tmp5:
            q += 1
        elif tmp2 < tmp1 and tmp2 < tmp3 and tmp2 < tmp4 and tmp2 < tmp5:
            w += 1
        elif tmp3 < tmp1 and tmp3 < tmp2 and tmp3 < tmp4 and tmp3 < tmp5:
            e += 1
        elif tmp4 < tmp1 and tmp4 < tmp2 and tmp4 < tmp3 and tmp4 < tmp5:
            r += 1
        elif tmp5 < tmp1 and tmp5 < tmp2 and tmp5 < tmp3 and tmp5 < tmp4:
            t += 1
        else:
            y += 1
    wins = {'Вставки':q, 'Выбор':w, 'Пузырёк':e, 'Гномы':r, 'Подсчетом':t, 'Ничья':y}       # Если хотя бы 2 проверки одинаковые - ничья
    return wins


print(speed_champ())


'''
Топ 5:
Длина массива:                      1013        2967        4666        6787
1) Гномья сортировка                0.000411    0.000813    0.001035    0.001289
2) Сортировка подсчетом             0.000740    0.002122    0.003760    0.002670
3) Сортировка метотом выбора        0.033909    0.280799    0.947913    1.576898
4) Пузырьковая сортировка           0.043000    0.520334    1.174369    2.406298
5) Сортировка вставками             0.071075    0.792398    1.980789    3.719482

{'Вставки': 0, 'Выбор': 0, 'Пузырёк': 0, 'Гномы': 9, 'Подсчетом': 1, 'Ничья': 0}

Во всех случаях наблюдается большой разрыв между алгоритмами
'''