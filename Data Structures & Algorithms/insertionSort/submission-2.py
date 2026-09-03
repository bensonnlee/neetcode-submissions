# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        """
        2 1 3
        """
        states = []
        for i in range(len(pairs)):
            while i > 0 and pairs[i].key < pairs[i-1].key:      
                pairs[i-1], pairs[i] = pairs[i], pairs[i-1]
                i -= 1
            states.append(pairs[:])

        return states