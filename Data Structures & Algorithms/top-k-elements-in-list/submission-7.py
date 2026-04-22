from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_h = []
        hashset = defaultdict(int)
        for num in nums:
            hashset[num] += 1

        for key,val in hashset.items():
            heapq.heappush(max_h, (val, key))
            if len(max_h) > k:
                heapq.heappop(max_h)
        res = []
        print(max_h)
        for key,val in max_h:
            res.append(val)

        return res