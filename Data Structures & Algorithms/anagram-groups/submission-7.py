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

        result = {}

        for string in strs:                          
            sorted_string = "".join(sorted(string)) 

            if sorted_string in result:
                result[sorted_string].append(string)
                continue
            result[sorted_string] = [string]

        return list(result.values())


        # step 5:
        # Time: (n * m log m) + n -> O(n * m log m)
        # space: O(n)
        
