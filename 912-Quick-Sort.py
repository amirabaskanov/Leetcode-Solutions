import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Average time: O(n log n)
        # Worst time:   O(n²)

        # Average recursion space: O(log n)
        # Worst recursion space:   O(n)
        
        def quicksort(nums, start, end):
            if start < end:
                # Partition the array to get the pivot index
                pi = partition(nums, start, end)
                # Recursively sort the elements before and after partition
                quicksort(nums, start, pi)
                quicksort(nums, pi + 1, end)
        
        def partition(nums, start, end):
            # pivot = nums[(start + end) // 2] #pivot element is the middle element
            pivot = nums[random.randint(start, end)] #using random to pass a leetcode quicksort killer
            i = start - 1
            j = end + 1

            while True:
                # Move i to the right until an element >= pivot is found
                i += 1
                while nums[i] < pivot:
                    i += 1
                # Move j to the left until an element <= pivot is found
                j -= 1
                while nums[j] > pivot:
                    j -= 1
                
                # If i crosses j, return j
                if i >= j:
                    return j
                
                nums[i], nums[j] = nums[j], nums[i]
            
        quicksort(nums, 0, len(nums) - 1)

        return nums
