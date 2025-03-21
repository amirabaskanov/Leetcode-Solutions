class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = {}

        for i in nums:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1

        sorted_table = sorted(table.items(), key = lambda item: item[1], reverse = True)

        print(sorted_table)

        out = []
        j = 0
        while j < k:
            out.append(sorted_table[j][0])
            j+=1

        return out
