class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        hi = len(nums) - 1
        while low <= hi:
            mid = (low + hi) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                hi = mid -1
        return -1
        
