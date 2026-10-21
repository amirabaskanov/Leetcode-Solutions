class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        visited_index = set()

        def getNext(index, curr_dir):
            next_index = (index + nums[index]) % n
            next_dir = 1 if nums[next_index] > 0 else -1
            if curr_dir != next_dir or index == next_index:
                return -1
            return next_index

        for i in range(n):
            if i in visited_index:
                continue
            slow, fast = i, i
            curr_dir = 1 if nums[i] > 0 else -1

            while True:
                visited_index.add(slow)
                visited_index.add(fast)

                slow = getNext(slow, curr_dir)
                fast = getNext(fast, curr_dir)

                if slow == -1 or fast == -1:
                    break
                
                fast = getNext(fast, curr_dir)

                if fast == -1:
                    break
                
                if slow == fast:
                    return True
        return False
