from typing import List
import math


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    arr = []
    for sub_arr in nested_arr:
        largest = float('-inf')
        for num in sub_arr:
            largest = max(largest, num)
        arr.append(largest)

    return arr


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
