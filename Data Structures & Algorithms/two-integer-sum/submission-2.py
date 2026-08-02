class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sum_target = {}
        
        for i, currentNum in enumerate(nums):
            complement = target - currentNum

            if complement in nums_sum_target.keys():
                return [nums_sum_target.get(complement), i]
            
            nums_sum_target[currentNum] = i

        return []