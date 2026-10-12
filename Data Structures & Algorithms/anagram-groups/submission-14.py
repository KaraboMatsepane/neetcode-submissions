class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

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
        
