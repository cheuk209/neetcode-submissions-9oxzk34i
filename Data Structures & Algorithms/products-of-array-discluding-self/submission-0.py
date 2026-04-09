import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_product = math.prod(nums)
        result_nums = [0] * len(nums)
        print(result_nums)
        for i in range(len(nums)):
            result_nums[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:])
        return result_nums
