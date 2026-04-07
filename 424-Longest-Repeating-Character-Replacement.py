class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        count = {}
        longest = 0

        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r-l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            longest = max(longest, r - l + 1)

        return longest
