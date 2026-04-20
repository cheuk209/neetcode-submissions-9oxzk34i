class Solution:
    def rob(self, nums: List[int]) -> int:
        # goal is to maximise value
        broken_into = {}
        return self.dynamic_rob(nums, len(nums)-1, broken_into)

    
    def dynamic_rob(self, nums, house, cache):
        if house == 0:
            return nums[house]

        # base case
        if house == 1:
            return max(nums[house], nums[house-1])
        
        if house in cache:
            return cache[house]


        max_value = max( self.dynamic_rob(nums, house-1, cache), self.dynamic_rob(nums, house-2, cache) + nums[house])
        cache[house] = max_value
        return max_value

    
