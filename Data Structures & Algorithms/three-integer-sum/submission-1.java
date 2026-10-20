class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<>();

        // outer loop: loop through array

        for (int i = 0; i < nums.length; i++) {
    
            int first = nums[i];

            int start = i + 1;

            int end = nums.length - 1;

            while (start < end) {
                int sum = first + nums[start] + nums[end];

                if (sum == 0){
                    List<Integer> triplet = List.of(first, nums[start++], nums[end--]);

                    if (!result.contains(triplet)){
                        result.add(triplet);
                    }
                    
                } else if (sum > 0){
                    --end;
                }else{
                    ++start;
                }
            }

        }

        return result;
    }
}
