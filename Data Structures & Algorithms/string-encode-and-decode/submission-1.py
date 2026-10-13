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
            word_length = ""
            while s[i] != "#":
                word_length += s[i]
                i += 1

            word_length = int(word_length)

            start = i + 1
            end = start + word_length
            word = s[start:end]
            result.append(word)
            i = end
            # for j in range((i + 1), (i + 1 + word_length)):
            #     word += s[j]
            #     i += 1
            # result.append(word)
            # i += 1
        return result





                