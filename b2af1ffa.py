from typing import List

def insert_sort(a: List[int]) -> List[int]:
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
    return a

if __name__ == '__main__':
    print(insert_sort([2, 1, 3, 4]))
