class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        import re
        s = s.lower()
        s = re.sub("[^a-z0-9]+", '', s)
        print(s)
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False
