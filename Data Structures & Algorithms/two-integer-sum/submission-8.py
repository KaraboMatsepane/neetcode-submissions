class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: nums (int array) and target int
        # list of i and j (indices) such that nums[i] + nums[j] 
        # == target, and i != j. smaller index first
        # constraints: i cannot be equal to j

        #step 2:
        # example nums = [1,3 5 8], target = 8 returns [3,5]

        #step 3:
        # what must be done repeatedly: add 2 numbers to see if
        # they equal target
        # structure?

        #step 4:

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [min(i, j), max(i, j)]

        # step 5:
        # time: O(n^2)
        # space: O (1) (no new variables/ data structures created)


        #step6:

        numbers = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in numbers.keys():
                return [min(i, numbers[diff]), max(i, numbers[diff])]
            numbers[num] = i

        
                

                    
                