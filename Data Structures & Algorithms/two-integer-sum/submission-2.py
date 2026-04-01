class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            print("num", num, "index", index)
            differential = target - num
            if differential in hashmap:
                return [hashmap[differential], index]
            hashmap[num] = index
        return hashmap