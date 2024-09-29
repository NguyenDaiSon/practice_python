from typing import List, Optional

def find_min(a: List[int]) -> Optional[int]:
    n = len(a)
    if n == 0:
        return None

    left, right = 0, n - 1
    index = 0

    while left <= right:
        mid = left + (right - left)//2

        if a[mid] <= a[-1]:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return a[index]


if __name__ == '__main__':
    print(find_min([3,4,5,1,2]))
    print(find_min([4,5,6,7,0,1,2]))
    print(find_min([11,13,15,17]))
    print(find_min([]))
