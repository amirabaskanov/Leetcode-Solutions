class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k   # convert to kth index in ascending order

        def quickSelect(l, r):
            pivot = nums[r]

            # [l, low)       < pivot
            # [low, mid)     == pivot
            # [mid, high]    unknown
            # (high, r]      > pivot
            low = l
            mid = l
            high = r

            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1

                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1

                else:
                    mid += 1

            # nums[l:low]          < pivot
            # nums[low:high + 1]   == pivot
            # nums[high + 1:r + 1] > pivot

            if k < low:
                return quickSelect(l, low - 1)

            elif k > high:
                return quickSelect(high + 1, r)

            else:
                return pivot

        return quickSelect(0, len(nums) - 1)
