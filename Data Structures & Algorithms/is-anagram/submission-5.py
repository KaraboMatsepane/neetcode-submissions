class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # //step 1:
        # //Input: two strings
        # //output: true if they are anagrams, otherwise false
        # //constraints: ?

        # //step 2: 
        # // racecar and carrace returns true,jar and jam returns
        # //false

        # //step 3: 
        # //what must be done repeatedly:for each ch in s, count 
        # // how many times it appears. for each ch in t, check if
        # //the count matches.
        # //Use Hashmap


        # //step 4:

        #step 5
        # time: O(n log n)
        # space: O(1) 
        # bottleneck: sorting

        #step 5: use Hashmap

        if len(s) != len(t):
            return False

        characters = {}

        for ch in s:
            #if already in map, add one. if not, add it and add 1

            characters[ch] = characters.get(ch, 0) + 1 

        for ch in t:
            characters[ch] = characters.get(ch, 0) - 1

        for value in characters.values():
            if value != 0:
                return False

        return True










        


