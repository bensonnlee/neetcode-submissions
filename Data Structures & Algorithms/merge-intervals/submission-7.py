class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                s = ans[-1][0]
                l = max(intervals[i][1], ans[-1][1])
                ans[-1] = [s, l]
            else:
                ans.append(intervals[i])

        return ans
