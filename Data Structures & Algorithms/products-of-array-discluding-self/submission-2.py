import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_nums = [0] * len(nums)
        suffix_nums = [0] * len(nums)

        prefix_nums[0] = 1
        suffix_nums[-1] = 1
        for i in range(1, len(nums)):
            prefix_nums[i] = prefix_nums[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1): 
            suffix_nums[i] = suffix_nums[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = prefix_nums[i] * suffix_nums[i]

        return nums