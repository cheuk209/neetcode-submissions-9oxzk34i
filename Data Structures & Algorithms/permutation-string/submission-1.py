from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashset = defaultdict(int)
        for s in s1:
            hashset[s] += 1
        L = 0
        substr = defaultdict(int)
        for R in range(len(s2)):
            substr[s2[R]] += 1

            if R-L == len(s1):
                substr[s2[L]] -= 1
                if substr[s2[L]] == 0:
                    substr.pop(s2[L])
                L += 1
            
            if substr == hashset:
                return True

            
        return False