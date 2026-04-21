class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs([], nums, res)
        return res

    def dfs(self, curr, nums, res):
        if curr not in res:
            res.append(curr.copy())
        

        for index, num in enumerate(nums):
            if num not in curr:
                curr.append(num)
                self.dfs(curr, nums[index:], res)
                curr.pop()
            else:
                continue
        return