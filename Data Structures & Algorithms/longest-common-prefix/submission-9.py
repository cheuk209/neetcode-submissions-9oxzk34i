class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        result_string = ""
        for i in range(len(first_word)):
            for s in strs:
                if i == len(s) or first_word[i] != s[i]:
                    return result_string
            result_string += first_word[i]
        return result_string