class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_seq = 1
        if len(nums) == 0:
            return 0
        for num in nums:
            current_seq = 1
            if num - 1 in hashset:
                continue
            else:
                while num + 1 in hashset:
                    current_seq += 1
                    num = num + 1
                    longest_seq = max(current_seq, longest_seq)
        
        return longest_seq