class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counter = 0
        zero_index = -1
        product_without_zeros = 1

        for idx, num in enumerate(nums):
            if num == 0:
                zero_index = idx
                zero_counter += 1
            else:
                product_without_zeros *= num
            
        ans = [0] * len(nums)

        if zero_counter == 0:
            for idx, num in enumerate(nums):
                ans[idx] = (product_without_zeros // num)
        elif zero_counter > 1:
            pass
        else:
            ans[zero_index] = product_without_zeros

        return ans