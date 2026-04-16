from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashset = defaultdict(int)
        longest_string = 1
        for right in range(len(s)):
            hashset[s[right]] += 1
            window_size = right - left + 1
            max_element = max(hashset.values())
            
            if window_size - max_element > k:
                hashset[s[left]] += -1
                left += 1
            longest_string = max(longest_string, sum(hashset.values()))
        return longest_string