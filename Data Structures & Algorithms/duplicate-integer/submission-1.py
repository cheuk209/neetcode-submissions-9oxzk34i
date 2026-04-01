class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                return True
            else:
                hashmap[i] = 1
        return False