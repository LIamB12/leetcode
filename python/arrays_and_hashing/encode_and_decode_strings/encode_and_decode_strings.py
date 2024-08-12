class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_array = []
        while i < len(s):
            strlen = ""
            while s[i] != "#":
                strlen += s[i]
                i += 1
            strlen = int(strlen)

            i += 1
            curr_string = ""

            if strlen == 0:
                decoded_array.append(curr_string)
                continue

            for _ in range(strlen):
                curr_string += s[i]
                i += 1

            decoded_array.append(curr_string)
        return decoded_array
            


