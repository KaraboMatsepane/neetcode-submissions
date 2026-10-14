class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        for i, num in enumerate(nums):

            if i == 0:
                result.append(1)

            else:
                prefix_left_most_number = nums[i - 1]
                prefix_arr_last_product = result[len(result) - 1]
                result.append(prefix_left_most_number * prefix_arr_last_product)

        suffix_product = 1
        
        for i in range(len(nums)-1, -1, -1):

            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result