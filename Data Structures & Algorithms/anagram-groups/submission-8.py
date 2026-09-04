class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: value
        # freq of char: the actual string
        # freq of char: [[cat, act]]
        # {a: 1, b: 2}: [[act, cat]]

        seen = {}

        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] = freq[ord(char) - ord('a')] + 1

            if str(freq) not in seen:
                seen[str(freq)] = [string]
            else:
                seen[str(freq)].append(string)
        
        return list(seen.values())
