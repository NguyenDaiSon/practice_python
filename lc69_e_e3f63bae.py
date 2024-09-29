from typing import List

def approximate_square_root(x: int) -> int:
    if x <= 1:
        return x

    index, left, right = -1, 1, x//2
    while left <= right:
        mid = left + (right - left)//2
        if mid == x/mid:
            index = mid
            break
        if mid < x/mid:
            index = mid
            left = mid + 1
        else:
            right = mid - 1
            index = right

    return index

if __name__ == '__main__':
    for i in range(0, 129):
        print("{} -> {}".format(i, approximate_square_root(i)))
