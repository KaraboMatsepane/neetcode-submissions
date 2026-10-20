class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int startIdx = 0;
        int endIdx = numbers.length -1;

        int[] result = new int[2];

        while (startIdx < endIdx){
            int sum = numbers[startIdx] + numbers[endIdx];

            if (sum == target) {
                result[0] = ++startIdx;
                result[1] = ++endIdx;
                return result;
            } else if (sum > target){
                --endIdx;
            } else {
                ++startIdx;
            }
        }

        return result;
    }
}
