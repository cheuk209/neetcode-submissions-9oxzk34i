class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, curr):
            if sum(curr) == target:
                result.append(curr.copy())
                return
            elif sum(curr) > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i, curr)
                curr.pop()
        
        backtrack(0, [])
        return result