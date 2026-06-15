class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #0 -> [-1]
        curMin, curMax = 1, 1 #1 is like a neutral value

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n) #[-1, 8]
            curMin = min(temp, n * curMin, n) #[-1, -8]
            res = max(res, curMax)
        return res
        #O(n), O(1) memory