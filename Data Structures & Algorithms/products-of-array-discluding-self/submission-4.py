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
                prefix.append(1)

            else:
                prefix_left_most_number = nums[i - 1]
                prefix_arr_last_product = prefix[len(prefix) - 1]
                prefix.append(prefix_left_most_number * prefix_arr_last_product)
        
        for i in range(len(nums)-1, -1, -1):

            if i == len(nums) -1:
                suffix.append(1)

            else:
                right_most_number = nums[i + 1]
                last_product = suffix[len(suffix) - 1]
                suffix.append(right_most_number * last_product)

        for i in range(len(nums)):
            prefix_num = prefix[i]
            suffix_num = suffix[len(nums) - 1 - i]

            result.append(prefix_num * suffix_num)

        return result


            



            



        
        #time: O(n^2)
        #space: O(n)

        