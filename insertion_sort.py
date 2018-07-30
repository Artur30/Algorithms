import random as rd
import time


def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j > -1 and lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1
            i -= 1
    return lst


if __name__ == '__main__':
    lst = [rd.randint(0, 100000) for _ in range(100)]
    time_start = time.time()
    insertion_sort(lst)
    time_end = time.time()
    print('Время работы insertion_sort:', time_end - time_start)
