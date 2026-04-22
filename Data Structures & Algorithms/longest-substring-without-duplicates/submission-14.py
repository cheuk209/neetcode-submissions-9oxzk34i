class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        L = 0
        max_string = 0
        for R in range(len(s)):
            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1
                continue
            hashset.add(s[R])
            print(R, L, R-L)
            max_string = max(max_string, R-L+1)

        return max_string