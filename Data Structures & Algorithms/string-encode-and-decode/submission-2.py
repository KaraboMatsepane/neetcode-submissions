class Solution:

    def encode(self, strs: List[str]) -> str:

        result = []

        for string in strs:
            to_append = "" + str(len(string)) + "#" + string
            result.append(to_append)

        return "".join(result)

            

    def decode(self, s: str) -> List[str]:

        result = []

        i = 0

        while i < len(s):   
            j = int(s.index("#", i))
            length = int(s[i:j])
        
            start = j + 1
            end = start + length
            word = s[start:end]
            result.append(word)
            i = end
        
        return result





                