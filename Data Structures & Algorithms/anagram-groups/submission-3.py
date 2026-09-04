class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: value
        # all letters sorted: the actual string
        # sorted(string): [[cat, act]]

        # create a list
            # create a sublist of each of the values

        seen = {}

        for string in strs:
            sorted_string = sorted(string)
            if str(sorted_string) in seen:
                seen[str(sorted_string)].append(string)
            else:
                seen[str(sorted_string)] = [string]

        return list(seen.values())
