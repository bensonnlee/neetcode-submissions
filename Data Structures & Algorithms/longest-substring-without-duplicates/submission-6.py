class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_len = 0

        """
              l
              r
        s = abba

        """
        for r in range(len(s)):
            # while s[r] in set, remove s[l], l += r
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            # add and re-calculate
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len