class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> match = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];

            if (match.containsKey(diff)) {
                return new int[] {match.get(diff), i};
            }
            match.put(nums[i], i);
        }
        return null;
    }
}
