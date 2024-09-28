from typing import List

def bubble_sort(a: List[int]) -> List[int]:
    n = len(a)
    for i in range(n-1, -1, -1):
        swapped = False
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

if __name__ == '__main__':
    print(bubble_sort([2, 1, 3, 4]))
