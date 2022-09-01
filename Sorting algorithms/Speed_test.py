import random
import time

def list_generator(minrange=100,maxrange=5000):
    for i in range(1):
        a = list(range(random.randint(minrange,maxrange)))                          
        random.shuffle(a)
    return a
random_list = list_generator()

def speed_test(func, number_of_rounds=10, *args):
    tmp = []
    for i in range(number_of_rounds):                               # Сюда вбить число раундов
        tic = time.perf_counter()
        func(*args)                                                 
        tac = time.perf_counter()
        tmp.append(tac - tic)
        print(f"Вычисление заняло {(tac - tic):0.6f} секунд")
    for i in range(len(tmp)-1):
        q = tmp[i] + tmp[i+1]
    print(f'Среднее время вычисления {(q/len(tmp)):0.7f} секунд')


def speed_test_sort(func, number_of_rounds=10):
    tmp = []
    for i in range(number_of_rounds):                               # Сюда вбить число раундов
        a = list_generator()                                       # Если понадобится генератор массивов для сортировки
        tic = time.perf_counter()
        func(a)                                                
        tac = time.perf_counter()
        tmp.append(tac - tic)
        print(f"Вычисление заняло {(tac - tic):0.6f} секунд")
    for i in range(len(tmp)-1):
        q = tmp[i] + tmp[i+1]
    print(f'Среднее время вычисления {(q/len(tmp)):0.7f} секунд')


def speed_test_compare(func1, func2, nor=10, *args):   # args это список/ки которые нужно отсортировать
    tmp1 = []
    tmp2 = []
    for i in range(nor):                               # Сюда вбить число раундов
        tic = time.perf_counter()
        func1(*args)                                                 
        tac = time.perf_counter()
        tmp1.append(tac - tic)
        tic = time.perf_counter()
        func2(*args)                                                 
        tac = time.perf_counter()
        tmp2.append(tac - tic)
    for i in range(len(tmp1)-1):
        q1 = tmp1[i] + tmp1[i+1]
    for i in range(len(tmp2)-1):
        q2 = tmp2[i] + tmp2[i+1]
    print(f'Сортировали такой список: {random_list}')
    print(f'Разница в скорости между функциями {(q1/len(tmp1) - q2/len(tmp2)):0.7f} секунд')
    return




