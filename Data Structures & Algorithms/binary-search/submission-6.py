class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        """            l
                           r
                     
        nums = [-1,0,2,4,6,8], target = 4


        """

        while l <= r:
            mid = (r - l) // 2 + l

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1