class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        entire_product = 1
        zero_count = 0
        zero_idx = -1

        for idx, num in enumerate(nums):
            if num == 0:
                zero_idx = idx
                zero_count += 1

            if num == 0 and zero_count == 1:
                pass
            else:
                entire_product *= num

        ans = [0] * len(nums)

        if zero_count == 1:
            ans[zero_idx] = entire_product
            return ans

        if zero_count == 2:
            return ans

        for i in range(len(nums)):
            if nums[i] == 0:
                ans[i] = entire_product
            else:
                ans[i] = entire_product // nums[i]

        return ans