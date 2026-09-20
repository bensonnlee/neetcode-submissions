class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True

        if len(s) > len(t):
            return False
        
        t_ptr = 0
        count = 0
        for char_s in s:
            if t_ptr == len(t):
                return False
            while char_s != t[t_ptr] and t_ptr < len(t) - 1:
                t_ptr += 1
            count += 1
            t_ptr += 1

        if count == len(s):
            return True
        return False