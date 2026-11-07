from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l = 0
        hashmap = defaultdict(int)
        hashmap2 = defaultdict(int)
        for s in range(len(s1)):
            hashmap[s1[s]] += 1
        for r in range(len(s2)):
            hashmap2[s2[r]] += 1
            
            if r - l  == k:
                hashmap2[s2[l]] -= 1
                if hashmap2[s2[l]] == 0:
                    del hashmap2[s2[l]]
                l += 1
            
            if  hashmap == hashmap2:
                return True
            
        return False