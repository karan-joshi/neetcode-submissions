class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = dict()

        for s in strs:
            set_s = "".join(sorted(s))

            if set_s in ana_map:
                ana_map[set_s].append(s)
            else:
                ana_map[set_s] = [s]

        result = []
        for key, val in ana_map.items():
            result.append(val)

        return result