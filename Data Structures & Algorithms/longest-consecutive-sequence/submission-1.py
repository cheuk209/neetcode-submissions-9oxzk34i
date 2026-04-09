class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        current = 1
        consecutive_count = 1
        max_count = 1
        if len(nums) == 0:
            return 0
        while current < len(nums):
            print(nums[current])
            if nums[current] == nums[current-1]:
                current += 1
                continue
            elif nums[current] == nums[current-1] + 1:
                consecutive_count += 1
                max_count = max(max_count, consecutive_count)
            else:
                consecutive_count = 1
            current += 1
        return max_count