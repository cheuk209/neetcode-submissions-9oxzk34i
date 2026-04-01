from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_hashmap = defaultdict(int)
        for num in nums:
            frequency_hashmap[num] += 1
        
        shift_delete_operation = 0
        results = []
        while shift_delete_operation < k:
            max_key = max(frequency_hashmap, key=frequency_hashmap.get)
            results.append(max_key)
            del frequency_hashmap[max_key]
            shift_delete_operation += 1
        return results
        
        