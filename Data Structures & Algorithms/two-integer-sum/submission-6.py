class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        # iterate through the list
        for i in range(len(nums)):

            # find a value to find in the hash map
            diff = target - nums[i]

            # if the value is found, return the value's index, then i
            if diff in hash_map.keys():
                return [hash_map[diff], i]
            
            # otherwise, store it in the hash map
            else:
                hash_map[nums[i]] = i

        return []