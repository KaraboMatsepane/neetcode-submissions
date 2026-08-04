class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dict1 ={}
        
        
        for anagram in strs:
            
            sorted_anagram = "".join(sorted(anagram))
            
            if sorted_anagram in dict1:
                dict1[sorted_anagram].append(anagram)
                continue
                
            dict1[sorted_anagram] = [anagram]
        
        return [lst for lst in dict1.values()]
        