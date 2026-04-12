class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid_point = (left + right) // 2
            mid_point_value = nums[mid_point]
            if mid_point_value < target:
                left = mid_point + 1
            elif mid_point_value > target:
                right = mid_point - 1
            else:
                return mid_point
        return -1