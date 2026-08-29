class Solution:

    def encode(self, strs: List[str]) -> str:
        combinedstr = ""
        for string in strs:
            combinedstr += str(len(string)) + ":"
            combinedstr += string
        return combinedstr


    def decode(self, s: str) -> List[str]:
        decoded = []
        lengthofstring = 0
        while len(s) > 0:
            for i, letter in enumerate(s):
                if letter == ":":
                    lengthofstring = int(s[:i])
                    words = s[i + 1:i + 1 + lengthofstring]
                    break
            decoded.append(words)
            words = ""
            s = s[i + 1 + lengthofstring:]
        return decoded

