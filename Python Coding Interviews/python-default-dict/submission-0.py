from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1

    return freq


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    out = defaultdict(list)
    for arr in nums:
        for idx, num in enumerate(arr):
            if idx == 0:
                pass
            else:
                out[arr[0]].append(num)
    return out

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
