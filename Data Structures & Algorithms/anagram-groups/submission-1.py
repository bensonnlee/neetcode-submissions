class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: value
        # all letters sorted: the actual string
        # sorted(string): [[cat, act]]

        # create a list
            # create a sublist of each of the values

        seen = {}

        for string in strs:
            if str(sorted(string)) in seen:
                seen[str(sorted(string))].append(string)
            else:
                seen[str(sorted(string))] = [string]

        ans = []
        for key, value in seen.items():
            ans.append(value)

        return ans

