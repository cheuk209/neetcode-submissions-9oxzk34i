class Solution:
    def rob(self, nums: List[int]) -> int:
        # house arranged in a circle
        visited = {}
        if len(nums) == 1:
            return nums[0]
        first_path = nums[0:len(nums)-1]
        second_path = nums[1:len(nums)]
        first_res = self.dp(first_path, len(first_path)-1, visited)
        visited = {}
        second_res = self.dp(second_path, len(second_path)-1, visited)
        return max(first_res, second_res)

    def dp(self, nums, i, cache):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[i], nums[i-1])

        if i in cache:
            return cache[i]
        
        res = max( nums[i] + self.dp(nums, i-2, cache), self.dp(nums, i-1, cache))
        cache[i] = res
        return res