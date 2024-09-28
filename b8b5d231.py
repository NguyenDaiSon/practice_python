from typing import List

def select_sort(a: List[int]) -> List[int]:
    n = len(a)
    for i in range (0, n - 1):
        m = i
        for j in range (i, n):
            if a[j] < a[m]:
                m = j
        if m != i:
            a[m], a[i] = a[i], a[m]
    return a

if __name__ == '__main__':
    print(select_sort([2, 1, 3, 4]))
