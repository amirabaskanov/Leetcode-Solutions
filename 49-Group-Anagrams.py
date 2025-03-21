class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}

        for i in range(len(strs)):
            letterset = "".join(sorted(strs[i]))
            if letterset not in table:
                table[letterset] = [strs[i]]
            else:
                table[letterset].append(strs[i])

        return list(table.values())
