class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        return shortest substring of s, such that
        every character in t, including duplicates,
        is present in the substring
        --- 
            l
                  r
        s = AAZAAYX, t = XYZ
        need = {
            X: 1,
            Y: 1,
            Z: 1
        }
        have = {
            A: 4,
            Z: 1
            Y: 1
            Z: 1
        }
        """
        def satisfied(have, need) -> bool:
            for char, freq in need.items():
                if have.get(char, 0) < freq:
                    return False
            return True
        
        ans = None

        have = {}
        need = {}
        for char in t:
            need[char] = 1 + need.get(char, 0)

        l = 0
        for r in range(len(s)):
            have[s[r]] = 1 + have.get(s[r], 0)

            while have.get(s[l], 0) > need.get(s[l], 0) and l < r:
                have[s[l]] -= 1
                l += 1

            if satisfied(have, need):
                substring = s[l:r+1]
                if ans is None or len(substring) < len(ans):
                    ans = substring


        return ans if ans else ""














