class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Step 1:
        # Input : int array
        # Output: in array where array[i] is the product of all the numbers in the input array excluding input[i]
        # constraints:


        #step 2:
        # input : [1,2,4,6]
        # expected Output: [48, 24, 12, 8]

        # Step 3:
        # What to do repeatedly: for each number in nums, remove the number from the array and compute the product of the remaining numbers in nums
        # Data structure: HashMap


        # Step 4, brute force:
        suffix = []
        prefix = []

        result = []

        for i, num in enumerate(nums):

            if i == 0:
                result.append(1)

            else:
                prefix_left_most_number = nums[i - 1]
                prefix_arr_last_product = result[len(prefix) - 1]
                result.append(prefix_left_most_number * prefix_arr_last_product)

        suffix_product = 1
        
        for i in range(len(nums)-1, -1, -1):

            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result


        
        #time: O(n)
        #space: O(n)

        