class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_array = len(nums)
        get_set = set(nums)
        len_set = len(get_set)
        if len_set == len_array:
            return "false"
        return "true"
        