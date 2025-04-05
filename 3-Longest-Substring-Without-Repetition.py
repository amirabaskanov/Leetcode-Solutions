class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_length = 0 
        longest_set = set()

        for right in range(len(s)):
            while s[right] in longest_set:
                longest_set.remove(s[left])
                left += 1
            longest_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
        



