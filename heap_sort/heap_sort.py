lst = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def max_heapify(lst, i):
    l = 2 * i
    r = 2 * i + 1

    if l < len(lst) and lst[l] > lst[i]:
        largest = l
    else:
        largest = i
    if r < len(lst) and lst[r] > lst[largest]:
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heapify(lst, largest)


def build_max_heap(lst):
    for i in range(int(len(lst) / 2), -1, -1):
        max_heapify(lst, i)

ans_list = []
def heapsort(lst):
    build_max_heap(lst)
    for i in range(len(lst) - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        ans_list.append(lst.pop(-1))
        max_heapify(lst, 0)
    return ans_list

ls = heapsort(lst)
print(ls)
