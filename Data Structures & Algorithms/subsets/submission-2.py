class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(0, nums, [])
        return self.res

    def dfs(self, start, nums, curr):
        if curr not in self.res:
            self.res.append(curr.copy())
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.dfs(i+1, nums, curr)
            curr.pop()
        return