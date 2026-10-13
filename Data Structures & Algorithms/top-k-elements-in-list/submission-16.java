class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numCount = new HashMap<>();

        for (int num: nums){
            numCount.put(num, numCount.getOrDefault(num, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(numCount.entrySet());

        entryList.sort(Map.Entry.<Integer, Integer>comparingByValue().reversed());

        int[] result = new int[k];

        for (int i = 0; i < k; i++){
            result[i] = entryList.get(i).getKey();
        }


        return result;
    }
}
