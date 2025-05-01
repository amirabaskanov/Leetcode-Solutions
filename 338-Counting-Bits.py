class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = [0]

        while (len(ans) <= n): 
            ans.extend([i+1 for i in ans])
        return ans[:n+1]
