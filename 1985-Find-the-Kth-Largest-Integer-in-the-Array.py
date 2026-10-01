class Solution:
    def kthLargestNumber(self, nums_int: list[str], k: int) -> str:
        # Quickselect
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        nums = []
        for num in nums_int:
            nums.append(int(num))

        low, high = 0, len(nums) - 1

        k = len(nums_int) - k        

        while low <= high:
            pivot_index = random.randint(low, high)
            pivot = nums[pivot_index]

            lessthan = low
            greaterthan = high

            i = low
            while i <= greaterthan:
                if nums[i] < pivot:
                    nums[i], nums[lessthan] = nums[lessthan], nums[i]
                    i += 1
                    lessthan += 1
                
                elif nums[i] > pivot:
                    nums[i], nums[greaterthan] = nums[greaterthan], nums[i]
                    greaterthan -= 1

                else:
                    i += 1

            if k < lessthan:
                high = lessthan - 1      
            elif k > greaterthan:
                low = greaterthan + 1
            else:
                return str(nums[k])
