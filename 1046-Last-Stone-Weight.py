class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) #linear time operation

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones) #second stone is smaller or equal than first
            if second > first: #account for negative values ><
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
