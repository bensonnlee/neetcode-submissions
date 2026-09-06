class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        map = {
            sorted(s): [s, etc]
        }
        """
        seen = defaultdict(list)
        ans = []

        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            seen[tuple(counts)].append(s)

        return list(seen.values())
            