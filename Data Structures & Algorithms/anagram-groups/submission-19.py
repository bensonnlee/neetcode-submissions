class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        map = {
            sorted(s): [s, etc]
        }
        """
        seen = {}
        ans = []

        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            if tuple(counts) in seen:
                seen[tuple(counts)].append(s)
            else:
                seen[tuple(counts)] = [s]

        return list(seen.values())