class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Time:  O(n + m)
        # Space: O(n + m)

        # n = number of elements
        # m = max(nums) - min(nums) + 1

        def counting_sort(arr):
            min_value = min(arr) #Need to handle negative values
            max_value = max(arr) 

            # Initialize auxiliary array with 0
            aux = [0] * (max_value - min_value + 1)

            # Count the occurences of each element in arr
            for num in arr:
                aux[num - min_value] += 1

            # Calculate the prefix sum in the auxiliary array
            for i in range(1, len(aux)):
                aux[i] += aux[i -1]

            # Create the sorted array
            sorted_arr = [0] * len(arr)
            for num in reversed(arr):
                index = num - min_value

                sorted_arr[aux[index] -1] = num
                aux[index] -= 1
            
            return sorted_arr
        
        return counting_sort(nums)
