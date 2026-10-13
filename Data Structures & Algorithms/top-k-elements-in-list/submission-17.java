class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numCount = new HashMap<>();            

        for (int num: nums){                                         //n
            numCount.put(num, numCount.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] buckets = new List[nums.length + 1];

        for (int i = 0; i < buckets.length; i++){
            buckets[i] = new ArrayList<>();
        }

        for (Map.Entry<Integer, Integer> entry: numCount.entrySet()){
            buckets[entry.getValue()].add(entry.getKey());
        }

        List<Integer> result = new ArrayList<>();

        for (int i = buckets.length - 1; i > 0; i--){
            List<Integer> bucket = buckets[i];

            if (!bucket.isEmpty()){
                for (int num: bucket){
                    if(result.size() == k) return result.stream().mapToInt(Integer::intValue).toArray();

                    result.add(num);
                }

            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}