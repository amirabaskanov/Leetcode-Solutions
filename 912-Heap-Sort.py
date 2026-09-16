class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(nums, N, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < N and nums[left] > nums[largest]:
                largest = left
            if right < N and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, N, largest)

        def heap_sort(nums):
            N = len(nums)

            for i in range(N // 2 - 1, -1, -1):
                heapify(nums, N, i)
            for i in range(N - 1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(nums, i, 0)
            return nums

        return heap_sort(nums)
