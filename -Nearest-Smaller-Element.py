class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
		stack = []
		res = []
		
		for i in A:
			while stack and stack[-1] >= i:
				stack.pop()
			if stack:
				res.append(stack[-1])
			else:
				res.append(-1)
			stack.append(i)
		return res
