class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -----       i    j k
        nums = [-4,-1,-1,0,1,2]
        -----   i j k
        nums = [0,0,0]
        -----

        -nums[i] = nums[j] + nums[k]
        target = -nums[i]

        if nums[j] + nums[k] > target
            k -= 1
        if nums[j] + nums[k] < target
            j += 1
        if nums[j] + nums[k] == target
            add triplet
            j += 1 or k -= 1
        """
        seen = set()
        nums.sort()
        for i in range(len(nums) - 2):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    seen.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return list(seen)