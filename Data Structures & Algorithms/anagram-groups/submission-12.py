class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        map = {
            sorted(s): [s, etc]
        }
        """
        seen = {}
        for s in strs:
            if str(sorted(s)) in seen:
                seen[str(sorted(s))].append(s)
            else:
                seen[str(sorted(s))] = [s]

        ans = []
        for value in seen.values():
            ans.append(value)
        
        return ans