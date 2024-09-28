from typing import List

def quick_sort(a: List[int]) -> List[int]:
    quick_sort_impl(a, 0, len(a))
    return a

def quick_sort_impl(a: List[int], start: int, end: int):
    if end - start <= 1:
        return

    pivot = a[end-1]
    i, j = start, end-1

    while i < j:
        while a[i] < pivot and i < j:
            i += 1

        while a[j] >= pivot and i < j:
            j -= 1

        a[i], a[j] = a[j], a[i]

    a[i], a[end-1] = a[end-1], a[i]

    quick_sort_impl(a, start, i)
    quick_sort_impl(a, i+1, end)

if __name__ == '__main__':
    print(quick_sort([2, 1, 3, 4]))
