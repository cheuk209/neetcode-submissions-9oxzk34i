class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.target = target
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, curr):
        if sum(curr) == self.target:
            self.res.append(curr.copy())
        
        if sum(curr) > self.target:
            return
        
        for i in range(len(nums)):
            curr.append(nums[i])
            self.dfs(nums[i:], curr)
            curr.pop()
        return
