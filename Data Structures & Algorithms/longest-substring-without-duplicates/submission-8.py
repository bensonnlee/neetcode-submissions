class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        max_len = 0

        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            seen[char] = r
            max_len = max(max_len, r - l + 1)

        return max_len