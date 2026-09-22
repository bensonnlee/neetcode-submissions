class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        to_remove = []

        for i in range(len(intervals) - 1):
            if intervals[i][0] <= intervals[i + 1][0] <= intervals[i][1]:
                # adopt the smallest [0] and the largest [1]
                smallest = min(intervals[i][0], intervals[i + 1][0])
                largest =  max(intervals[i][1], intervals[i + 1][1])
                intervals[i + 1] = [smallest, largest]
                to_remove.append(i)
        
        to_remove.sort(reverse=True)
        for i in to_remove:
            del intervals[i]

        return intervals
