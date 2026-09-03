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
        for i in range(0, len(pairs)):
            while i > 0 and pairs[i].key < pairs[i-1].key:      
                tmp = pairs[i-1]
                pairs[i-1] = pairs[i]
                pairs[i] = tmp
                i -= 1
                
            arr = []

            for pair in pairs:
                arr.append((pair))
            states.append(arr)

        return states