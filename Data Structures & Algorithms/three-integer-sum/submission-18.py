class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        for i in range(len(nums) - 2):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k - 1 and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
            
        return ans