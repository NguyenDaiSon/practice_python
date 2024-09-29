from typing import List, Optional

def binary_search(a: List[int], target: int) -> Optional[int]:
    left, right = 0, len(a)-1
    while left <= right:
        middle = left + (right - left)//2
        if a[middle] == target:
            return middle
        if a[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return None

if __name__ == '__main__':
    print(binary_search([], 0))
    print(binary_search([1], 2))
    for i in range(0, 5):
        print(binary_search([1, 2, 3, 4], i))
