import random as rd
import time
import sys


def partition_lomuto(lst, p, r):
    """ Разбиение Ломуто """
    x = lst[r]
    i = p - 1
    
    for j in range(p, r):
        if lst[j] <= x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[r] = lst[r], lst[i + 1]
    return i + 1


def quick_sort_lomuto(lst, p, r):
    """ Быстрая сортировка с разбиением Ломуто """
    if p < r:
        q = partition_lomuto(lst, p, r)
        quick_sort_lomuto(lst, p, q - 1)
        quick_sort_lomuto(lst, q + 1, r)
    return lst


def partition_hoara(lst, p, r):
    """ Разбиение Хоара """
    x = lst[p]
    i = p
    j = r

    while True:
        while lst[i] < x and i < r:
            i += 1
        while lst[j] > x and j > p:
            j -= 1
        
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
        else:
            return j


def quick_sort_hoara(lst, p, r):
    """ Быстрая сортировка с разбиением Хоара """
    if p < r:
        q = partition_hoara(lst, p, r)
        quick_sort_hoara(lst, p, q - 1)
        quick_sort_hoara(lst, q + 1, r)
    return lst



if __name__ == '__main__':
    # lst = [rd.randint(0, 40) for _ in range(20)]
    """ Как мы видим быстрая сортировка с разбиением Хоара работает чуть быстрее.
        Это все конечно хорошо, но если у нас будет очень большое массив 
        (пускай 10000 элементов), то ничего не получится, так как будет очень большая
        глубина рекурсии, поэтому надо задать большую глубину рекурсии
    """
    # Устанавливаем большую глубину рекурсии
    sys.setrecursionlimit(1500)
    lst = [i for i in range(1000, -1, -1)]
    # print('Массив до сортировки:', lst)
    
    time_start = time.time()
    lomuto = quick_sort_lomuto(lst[:], 0, len(lst) - 1)
    time_end = time.time()
    # print('Быстрая сортировка с разбиением Ломуто:', lomuto)
    print('Время quick_sort_lomuto:', time_end - time_start)

    time_start = time.time()
    hoar = quick_sort_hoara(lst[:], 0, len(lst) - 1)
    time_end = time.time()
    # print('Быстрая сортировка с разбиением Хоара:', hoar)
    print('Время quick_sort_hoara:', time_end - time_start)

