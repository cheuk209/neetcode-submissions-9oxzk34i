class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for string in strs:
            string = f"{len(string)}£{string}"
            encode.append(string)
        return "".join(encode)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "£":
                j += 1
            decode_len = int(s[i:j])
            sample = s[j+1:j+decode_len+1]
            res.append(sample)
            i = j + decode_len + 1
            
        return res