class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        stack = []

        for i in range(len(s)):
            if s[i] not in map.values():
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    match = stack.pop()
                    if s[i] != map[match]:
                        return False
                else:
                    return False


        if len(stack) == 0:
            return True
        
        return False