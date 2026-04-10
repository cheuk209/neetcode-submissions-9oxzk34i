class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_triplets = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + target == 0:
                    result_triplets.append([target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    right += -1
                elif nums[left] + nums[right] + target < 0:
                    if nums[left+1]:
                        while nums[left] == nums[left+1]:
                            left += 1
                    left += 1
                else:
                    right += -1
        return result_triplets