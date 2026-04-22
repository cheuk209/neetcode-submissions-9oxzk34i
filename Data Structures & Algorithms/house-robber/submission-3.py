class Solution:
    def rob(self, nums: List[int]) -> int:
        visited = {}
        max_val = 0
        for i in range(len(nums)):
            max_val = max(self.dp(nums, i, visited), max_val)
        return max_val


    def dp(self, nums, n, cache):
        # base case
        if n == 0:
            return nums[n]
        if n == 1:
            return max(nums[n], nums[n-1])

        if n in cache:
            return cache[n]

        max_val = max(nums[n] + self.dp(nums, n-2, cache), self.dp(nums, n-1, cache))
        cache[n] = max_val
        return max_val