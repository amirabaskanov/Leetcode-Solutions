class Solution:
    nums = [1,2,3]
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(perm, used, permutations):
            if len(perm) == len(nums):
                permutations.append(perm[:])
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue

                perm.append(num)
                used[i] = True
                dfs(perm, used, permutations)
                # recursion
                perm.pop()
                used[i] = False
            
        permutations = []
        dfs([], [False] * len(nums), permutations)
        return permutations
