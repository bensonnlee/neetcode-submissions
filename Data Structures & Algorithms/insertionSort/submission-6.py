# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        states = [list(pairs)]

        for i in range(1, len(pairs)):
            item = pairs[i]
            j = i - 1
            while j >= 0 and pairs[j].key > item.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = item
            states.append(list(pairs))

        return states