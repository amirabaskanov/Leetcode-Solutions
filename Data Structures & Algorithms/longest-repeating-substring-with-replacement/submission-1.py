class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #character count 26
        res = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k: # r - l + 1 is length of the window & max value in the char count
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res