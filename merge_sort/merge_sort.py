lst = [2, 4, 5, 7, 1, 2, 3, 6]

def merge_sort(lst, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q, r)
    return lst
def merge(lst, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []; R = []

    L = [lst[p + i] for i in range(n1)]
    R = [lst[q + i + 1] for i in range(n2)]

    L.append(30000000)
    R.append(30000000)

    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1

ans_list = merge_sort(lst, 0, len(lst) - 1)
print(ans_list)