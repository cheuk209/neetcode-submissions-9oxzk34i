from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        results = []
        for num in nums:
            hashmap[num] += 1
        
        print(hashmap)
        for _ in range(k):
            top_element = max(hashmap, key=hashmap.get)
            print("what is top element", top_element)
            results.append(top_element)
            del hashmap[top_element]
        return results
