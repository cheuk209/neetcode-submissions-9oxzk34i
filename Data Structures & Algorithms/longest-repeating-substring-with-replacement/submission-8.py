class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = defaultdict(int)
        longest_substring = 0
        for right, val in enumerate(s):
            hashmap[s[right]] += 1
            max_element = max(hashmap.values())
            window_size = sum(hashmap.values())
            print("1. window size is: ", window_size)
            print("2. max element is ", max_element)
            print("3. hashmap contains: ", hashmap)
            if window_size - max_element > k:
                hashmap[s[left]] += -1
                left += 1
            longest_substring = max(longest_substring, sum(hashmap.values()))
        return longest_substring

        