class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_char = []
        for char in s:
            if char.isalnum():
                alpha_char.append(char)

        left_ptr = 0
        right_ptr = len(alpha_char) - 1

        while left_ptr < right_ptr:
            if alpha_char[left_ptr].lower() != alpha_char[right_ptr].lower():
                print(alpha_char[left_ptr])
                print(alpha_char[right_ptr])
                return False
            left_ptr += 1
            right_ptr -= 1

        return True