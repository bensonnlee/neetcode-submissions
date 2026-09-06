class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            if str(sorted(s)) in seen:
                seen[str(sorted(s))].append(s)
            else:
                seen[str(sorted(s))] = [s]
        
        return list(seen.values())