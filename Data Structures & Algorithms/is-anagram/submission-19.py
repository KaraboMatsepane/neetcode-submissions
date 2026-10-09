class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False

        characters = {}

        for i in range(len(s)):
            characters[s[i]] = characters.get(s[i], 0) + 1 
            characters[t[i]] = characters.get(t[i], 0) - 1

        for num in characters.values():
            if num != 0:
                return False

        return True










        


