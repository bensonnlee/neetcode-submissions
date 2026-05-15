class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division solution

        # if there are two zeros, entire array is 0
        # DONE

        # if there is one zero, everything except for
        # the index that has zero is zero

        # else, divide each index by the entire product

        zero_count = 0
        zero_idx = -1
        entire_product = 1
        ans = [0] * len(nums)

        for idx, num in enumerate(nums):
            if num == 0:
                zero_idx = idx
                zero_count += 1

        if zero_count > 1:
            return ans

        if zero_count == 1:
            for idx, num in enumerate(nums):
                if idx != zero_idx:
                    entire_product *= num
            ans[zero_idx] = entire_product

            return ans

        for num in nums:
            entire_product *= num

        return [entire_product // num for num in nums]