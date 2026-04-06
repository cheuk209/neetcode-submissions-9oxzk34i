class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for each_str in strs:
            encoded_str += str(len(each_str)) + "#" + each_str
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decoded_result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded_result