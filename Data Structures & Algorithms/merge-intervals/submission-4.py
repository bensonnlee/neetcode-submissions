class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort the intervals by their first number

        determine whether or not intervals[0] and intervals[1] are overlapping

        for example
        [1, 3] and [2, 5] and [3, 6] and [10, 11]
        
        are they overlapping?
        
        yes, because 2 is in the range of [1, 3]

        so then i can merge the two into
        [1, 5]

        then 3 is in the range of [1, 5]
        so becomes [1, 6]

        10 is not in the range of [1, 6]
        so list becomes [1,6] and [10, 11]
        """
        intervals.sort()
        ans = intervals[:]
        to_remove = []

        for i in range(len(intervals) - 1):
            if ans[i][0] <= ans[i + 1][0] <= ans[i][1]:
                # adopt the smallest [0] and the largest [1]
                smallest = min(ans[i][0], ans[i + 1][0])
                largest =  max(ans[i][1], ans[i + 1][1])
                ans[i + 1] = [smallest, largest]
                to_remove.append(i)
        
        to_remove.sort(reverse=True)
        for i in to_remove:
            del ans[i]

        return ans
