class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        key: value
        sorted string: actual string
        """
        seen = {}

        for s in strs:
            if str(sorted(s)) in seen:
                seen[str(sorted(s))].append(s)
            else:
                seen[str(sorted(s))] = [s]
            
        ans = []
        for values in seen.values():
            ans.append(values)

        return ans