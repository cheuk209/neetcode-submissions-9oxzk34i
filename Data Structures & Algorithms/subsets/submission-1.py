class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, curr):
        if curr not in self.res:
            self.res.append(curr.copy())
        
        for i in range(len(nums)):
            curr.append(nums[i])
            self.dfs(nums[i+1:], curr)
            curr.pop()
        return