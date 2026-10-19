class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = set(nums)

        longest = 0

        for num in nums:
            current = 0
            if (num - 1) not in nums:
                current += 1

                i = 1

                while ((num + i) in nums):
                    current += 1
                    i += 1
            if current > longest:
                longest = current

        return longest

        
        