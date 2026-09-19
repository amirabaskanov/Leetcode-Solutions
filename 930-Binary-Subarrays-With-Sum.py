class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        res = 0
        curr_sum = 0

        freq = {}

        for num in nums:
            curr_sum += num
            if curr_sum == goal:
                res += 1
            
            if curr_sum - goal in freq:
                res += freq[curr_sum - goal]

            freq[curr_sum] = freq.get(curr_sum, 0) + 1
        
        return res
