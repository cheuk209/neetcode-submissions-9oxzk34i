class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for each_strs in strs:
            encoded_str += str(len(each_strs)) + "%" + each_strs
        return encoded_str 
    def decode(self, s: str) -> List[str]:
        results_strings = []
        i = 0
        while i < len(s):
            delimiter_index = s.find("%", i)
            expected_len = int(s[i:delimiter_index]) # extract the len integer, stopping at the delimiter
            substring = s[delimiter_index + 1 : delimiter_index + 1 + expected_len]
            results_strings.append(substring)
            i = delimiter_index + 1 + expected_len
        return results_strings