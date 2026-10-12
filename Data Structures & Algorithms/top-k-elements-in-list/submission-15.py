class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1:
        # Input: int array nums, int k
        # output: k most frequent element
        # Constraints :
        # 1 <= nums.length <= 10^4
        # -1000 <= nums[i] <= 1000
        # 1 <= k <= number of distinct elements in nums

        #step 2:
        # Example: [1,2,3,3,5] k = 1 outputs 3

        #step 3:
        # what must repeatedly be done: for each num in nums, check its count and save it.
        # HashMap to save the number with its count

        # Step 4

        num_count = {}


        for num in nums:                 
            num_count[num] = num_count.get(num, 0) + 1


        buckets = [[] for _ in range(len(nums) + 1)]    

        for num, count in num_count.items():             
            buckets[count].append(num)

        result = []

        for bucket in buckets[::-1]:
                                  

            if bucket:
                for num in bucket:
                    if len(result) == k:
                        break
                    result.append(num)
                    

        return result
        


        # time: O(n)
        # space: O(n)



        


        