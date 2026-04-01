class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        print(len(nums_set), "vs", len(nums))
        if len(nums_set) == len(nums):
            return False
        return True