lst = [3, 4, 2, 8, 5, 6, 7, 1]

def quick_sort(lst, p, r):
    if p < r:
        q = partition(lst, p, r)
        quick_sort(lst, 0, q - 1)
        quick_sort(lst, q + 1, r)
    return lst
def partition(lst, p, r):
    x = lst[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if lst[j] <= x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[r - 1] = lst[r - 1], lst[i + 1]
    return i + 1

ans_lst = quick_sort(lst, 0, len(lst))
print(ans_lst)