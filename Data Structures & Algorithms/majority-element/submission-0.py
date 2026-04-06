from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        get_len = len(nums)
        majority_hashmap = defaultdict(int)
        for num in nums:
            majority_hashmap[num] += 1
            if majority_hashmap[num] > (get_len/2):
                return num