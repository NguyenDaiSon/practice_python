from typing import List

def merge_sort(a: List[int]) -> List[int]:
    n = len(a)
    if n <= 1:
        return a

    l, r = partition(a)
    l = merge_sort(l)
    r = merge_sort(r)
    a = merge(l, r)
    return a

def partition(a: List[int]) -> (List[int], List[int]):
    n = len(a)
    if n <= 1:
        return a, None
    return a[:n//2], a[n//2:]

def merge(l: List[int], r: List[int]) -> List[int]:
    a = []
    nl = len(l)
    nr = len(r)

    i, j = 0, 0
    while i < nl and j < nr:
        if l[i] < r[j]:
            a.append(l[i])
            i += 1
        else:
            a.append(r[j])
            j += 1

    while i < nl:
        a.append(l[i])
        i += 1

    while j < nr:
        a.append(r[j])
        j += 1

    return a

if __name__ == '__main__':
    print(merge_sort([2, 1, 3, 4]))
