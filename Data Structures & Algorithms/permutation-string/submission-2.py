from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation_len = len(s1)
        l = 0
        hashset = defaultdict(int)
        for char in s1:
            if char not in hashset:
                hashset[char] = 1
            else:
                hashset[char] += 1
        r = 0
        r_hashset = defaultdict(int)
        while r < len(s2):
            r_hashset[s2[r]] += 1
            if r - l + 1 == permutation_len:
                print("we are here", r_hashset, hashset)
                if hashset == r_hashset:
                    return True
                else:
                    r_hashset[s2[l]] -= 1
                    if r_hashset[s2[l]] == 0:
                        del r_hashset[s2[l]]
                    l += 1
            r += 1
        return False
