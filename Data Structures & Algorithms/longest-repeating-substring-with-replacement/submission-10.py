from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        l = 0
        longest_str = 0
        for r in range(len(s)):
            hashmap[s[r]] += 1
            window_len = r - l + 1
            print(max(hashmap.values()))
            while window_len - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
                window_len = r - l + 1
            longest_str = max(window_len, longest_str)
        return longest_str