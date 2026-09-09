class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            "{": "}",
            "[": "]",
            "(": ")",
        }

        # input = ()
        # stack = 
        # val = (

        for char in s:
            if char in char_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if char != char_map[val]:
                    return False
        if stack:
            return False
        return True