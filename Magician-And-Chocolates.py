import heapq
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
		MOD = 10**9 + 7
		
		heap = [-x for x in B]
		heapq.heapify(heap)
		
		total = 0
		
		for i in range(A):
			chocolates = -heapq.heappop(heap)
			
			total += chocolates
			
			heapq.heappush(heap, -(chocolates // 2 ))
			
		return total % MOD
