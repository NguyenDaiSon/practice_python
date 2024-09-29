from typing import List, Optional

def find_boundary(a: List[int]) -> Optional[int]:
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left)//2
        if not a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    left = None if left >= len(a) else left
    return left

if __name__ == '__main__':
    print(find_boundary([]))
    print(find_boundary([True, True, True]))
    print(find_boundary([False, True, True]))
    print(find_boundary([False, False, False]))
