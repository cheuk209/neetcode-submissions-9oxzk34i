class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =  []
        nums = sorted(nums)
        for index,num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            
            l = index + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + num == 0:
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    l += 1
                elif nums[l] + nums[r] + num > 0:
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
        return res
