class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        """
        nums = [-2, 1, 1, 1, 1]
        """
        nums.sort()
        for i in range(len(nums) - 2):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] == target:
                    while nums[j] == nums[j + 1] and j < k - 1:
                        j += 1
                    while nums[k] == nums[k - 1] and k > j + 1:
                        k -= 1

                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1

        return ans