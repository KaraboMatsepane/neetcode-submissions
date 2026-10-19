class Solution {
    public int longestConsecutive(int[] nums) {

        Set<Integer> numsSet = new HashSet<>();

        for (int num: nums) numsSet.add(num);

        int longest = 0;

        for (int num: numsSet) {
            int current_longest = 0;

            if (!numsSet.contains(num - 1)) {
                current_longest += 1;
                int counter = 1;

                while (numsSet.contains(num + counter++)){
                    current_longest += 1;
                }

                if (current_longest > longest) longest = current_longest;
            }
        }

        return longest;
    }
}
