class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_length, length = 1, 1

        # base cases
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # initialize set with left ptr
        seen = set()
        seen.add(s[l])

        # keep adding length from the right until end
        while r < len(s):
            # if right_ptr is in seen, reset seen and increment left_ptr. set right_ptr to left_ptr + 1
            # and add left_ptr to seen
            if s[r] in seen:
                seen.clear()
                l += 1
                r = l + 1
                length = 1
                seen.add(s[l])
            # otherwise, increase length by 1 and set max_length = max(length, max_length
            else:
                seen.add(s[r])
                length += 1
                max_length = max(max_length, length)
                r += 1

        return max_length

    """
     l
      r
    dvdf
    seen = { v }
    length = 1
    max_length = 2
    """