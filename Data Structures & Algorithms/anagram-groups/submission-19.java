class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramGroups = new HashMap<>();

        for (String str: strs){
            int[] hashKey = new int[26];

            for (char ch: str.toCharArray()) {
                int index = ch - 'a';
                hashKey[index]++;
            }

            String hashKeyStr = Arrays.toString(hashKey);
            if (!anagramGroups.containsKey(hashKeyStr)) {
                anagramGroups.put(hashKeyStr, new ArrayList<>());
            }

            anagramGroups.get(hashKeyStr).add(str);
        }

        return new ArrayList<>(anagramGroups.values());
    }
}
