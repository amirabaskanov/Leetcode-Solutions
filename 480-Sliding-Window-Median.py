class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small, large = [], []
        delayed = {}
        small_size = large_size = 0

        # remove deleted numbers from the heap's top
        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if not delayed.get(num, 0):
                    break
                
                heapq.heappop(heap)
                delayed[num] -= 1
                if delayed[num] == 0:
                    del delayed[num]
                
        # keep small with the same number or one extra
        def rebalance():
            nonlocal small_size, large_size
            
            if small_size > large_size + 1:
                heapq.heappush(large, -heapq.heappop(small))
                small_size -= 1
                large_size += 1
                prune(small)

            elif small_size < large_size:
                heapq.heappush(small, -heapq.heappop(large))
                small_size += 1
                large_size -= 1
                prune(large)
            
        result = []

        for i, num in enumerate(nums):
            # 1. Add incoming number
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            rebalance()

            # 2. Remove outgoing number
            if i >= k:
                old = nums[i - k]
                delayed[old] = delayed.get(old, 0) + 1

                if old <= -small[0]:
                    small_size -= 1
                else:
                    large_size -= 1
                
                prune(small)
                prune(large)
                rebalance()
            
            # 3. Record median of a complete window
            if i >= k - 1:
                # Bound heap growth from lazy deletions
                if len(small) + len(large) > 2 * k:
                    window = sorted(nums[i-k+1:i+1])
                    mid = (k + 1) // 2
                    small = [-x for x in window[:mid]]
                    large = window[mid:]
                    heapq.heapify(small)
                    heapq.heapify(large)
                    small_size, large_size = mid, k - mid
                    delayed.clear()
                
                median = float(-small[0]) if k % 2 else (-small[0] + large[0]) / 2
                result.append(median)
        return result
