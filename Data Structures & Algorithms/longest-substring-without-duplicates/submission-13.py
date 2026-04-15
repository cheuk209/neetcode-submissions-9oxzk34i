class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate_hashset = set()
        L = 0
        longest_count = 1
        if len(s) == 0:
            return 0
        for R in range(0, len(s)):
            while s[R] in duplicate_hashset:
                print("duplicate detected", s[R])
                duplicate_hashset.remove(s[L])
                L += 1
                print("removing leftmost element", s[L])
            else:
                duplicate_hashset.add(s[R])
            print("where is R", R)
            print("where is L", L)
            longest_count = max(longest_count, R - L + 1)

        return longest_count 