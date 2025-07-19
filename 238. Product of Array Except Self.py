class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)

        prefix = [1]
        suffix = [1]
        answer = []

        j = 0
        k = 1
        e = 1
        f = 1
        while j < len(nums)-1:
            prefix.append(nums[j] * k)
            suffix.insert(0, nums[-e] * f)
            k = k * nums[j]
            j += 1
            f = f * nums[-e]
            e += 1
        
        i = 0
        while i < l:
            answer.append(prefix[i] * suffix[i])
            i += 1
        return answer
