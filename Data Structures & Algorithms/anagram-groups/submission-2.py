class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword not in groups:
                groups[sortedword] = []
            groups[sortedword].append(word)

        return list(groups.values())


        