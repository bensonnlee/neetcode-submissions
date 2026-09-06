class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        naive solution:
            sort all of the strings
            group strings that are equal with a hash map
        """
        res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)
        return list(res.values())