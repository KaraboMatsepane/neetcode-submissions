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

        s_sorted = sorted(s.lower())
        t_sorted = sorted(t.lower())

        return s_sorted == t_sorted



        


