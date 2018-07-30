def max_heapfy(lst, i):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = left if left < len(lst) and lst[i] < lst[left] else i
    largest = right if right < len(lst) and lst[largest] < lst[right] else largest

    if i != largest:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heapfy(lst, largest)


def build_max_heap(lst):
    for i in range(int(len(lst) / 2), -1, -1):
        max_heapfy(lst, i)


def heap_sort(lst):
    answer_list = []
    build_max_heap(lst)
    for i in range(len(lst) - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        answer_list.append(lst.pop(i))
        max_heapfy(lst, 0)
    return answer_list[::-1]


if __name__ == '__main__':
    lst = [i for i in range(15, -1, -1)]
    print('Список до сортировки:', lst)
    lst = heap_sort(lst)
    print('Список после сортировки:', lst)

