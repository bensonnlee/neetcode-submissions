class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: value
        # all letters sorted: the actual string
        # sorted(string): [[cat, act]]

        # create a list
            # create a sublist of each of the values

        seen = {}

        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string in seen:
                seen[sorted_string].append(string)
            else:
                seen[sorted_string] = [string]

        return list(seen.values())
