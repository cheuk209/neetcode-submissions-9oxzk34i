from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        results = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            hashmap[num] += 1
        
        for key, value in hashmap.items():
            results[value].append(key)

        real_results = []
        print(results)
        for i in range(len(results)-1, 0, -1):
            if results[i]:
                for result in results[i]:
                    real_results.append(result)
            if len(real_results) == k:
                break

        return real_results
