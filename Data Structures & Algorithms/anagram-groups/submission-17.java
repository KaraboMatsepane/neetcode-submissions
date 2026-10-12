class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramGroups = new HashMap<>();

        for (String str: strs){
            char[] strArray = str.toCharArray();
            Arrays.sort(strArray);
            String strSorted = Arrays.toString(strArray);

            if (!anagramGroups.containsKey(strSorted)) {
                anagramGroups.put(strSorted, new ArrayList<>());
            }

            anagramGroups.get(strSorted).add(str);
        }

        List<List<String>> anagramGroupsList = new ArrayList<>();

        for (List<String> anagramGroup: anagramGroups.values()) {
            anagramGroupsList.add(anagramGroup);
        }

        return anagramGroupsList;
    }
}
