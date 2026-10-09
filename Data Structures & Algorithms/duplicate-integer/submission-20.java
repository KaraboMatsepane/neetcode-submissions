class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for (int num: nums) seen.add(num);

        return seen.size() != nums.length;
    }
}