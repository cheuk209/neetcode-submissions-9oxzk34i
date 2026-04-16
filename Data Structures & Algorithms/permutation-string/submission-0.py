from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hashset = defaultdict(int)
        for s in s1:
            s1_hashset[s] += 1
        left = 0
        window_size = len(s1)
        s2_hashset = defaultdict(int)
        for right in range(len(s2)):
            if right - left + 1 > window_size:
                s2_hashset[s2[left]] += -1
                if s2_hashset[s2[left]] == 0:
                    del s2_hashset[s2[left]]
                left += 1
            s2_hashset[s2[right]] += 1
            if s2_hashset == s1_hashset:
                return True

        return False