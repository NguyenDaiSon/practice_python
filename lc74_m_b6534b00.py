from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    if rows == 0:
        return False
    cols = len(matrix[0])
    if cols == 0:
        return False
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = left + (right - left)//2
        val = matrix[mid//cols][mid%cols]
        if val == target:
            return True
        if val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == '__main__':
    print(search_matrix([[]], 0))
    print(search_matrix([[1]], 0))
    print(search_matrix([[1]], 1))
    print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
