from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = defaultdict(int)
        longest_string = 0
        for r in range(len(s)):
            hashmap[s[r]] += 1

            while hashmap[s[r]] > 1:
                hashmap[s[l]] -= 1
                l += 1

            longest_string = max(longest_string, r - l + 1)

        return longest_string