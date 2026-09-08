class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
    
            if i > 0 and nums[i] == nums[i - 1]:
                # if there are duplicates with i, skip
                continue

            if nums[i] > 0:
                # early exit, two positives can never equal a negative
                break

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[j] + nums[k]
                
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return ans