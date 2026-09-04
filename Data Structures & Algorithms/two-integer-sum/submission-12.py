class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val: index

        # go thru all nums
        for i in range(len(nums)):

            # look for the number u need
            diff = target - nums[i]

            # if u see that number, return
            if diff in seen:
                return [seen[diff], i]

            # otherwise add it to ur bank
            seen[nums[i]] = i