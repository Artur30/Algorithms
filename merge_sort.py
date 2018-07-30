def merge(lst, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left_list = [lst[i + p] for i in range(n1)]
    right_list = [lst[i + q + 1] for i in range(n2)]
    left_list.append(float('inf'))
    right_list.append(float('inf'))

    i = j = 0
    for k in range(p, r + 1):
        if left_list[i] <= right_list[j]:
            lst[k] = left_list[i]
            i += 1
        else:
            lst[k] = right_list[j]
            j += 1


def merge_sort(lst, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q, r)
    return lst


if __name__ == '__main__':
    lst = [i for i in range(5, -1, -1)]
    merge_sort(lst, 0, len(lst) - 1)
    print(lst)
