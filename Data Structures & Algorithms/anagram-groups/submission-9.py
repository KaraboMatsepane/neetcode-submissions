class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Step 1:
        # input: list of strings
        # output: list of anagrams groups 
        #Constraints: 

        #Step 2:
        # Example: ["act","pots","tops","cat","stop","hat"] input returns
        # [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # Step 3:
        # what to do repeatedly: for each string, check if it is an anagram of any other strings in the array.
        # Data structure:

        # Step 4:

        anagram_groups = {}

        for string in strs:

            key = [0] * 26

            for ch in string:
                index = ord(ch) - ord("a")
                key[index] += 1
                
            key_tuple = tuple(key)

            if key_tuple not in anagram_groups:
                anagram_groups[key_tuple] = []
            
            anagram_groups[key_tuple].append(string)

        return list(anagram_groups.values())


        
