from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for word in strs:
            ordered_word = sorted(word)
            ordered_word = "".join(ordered_word)
            hashset[ordered_word].append(word)
        res = []
        for v in hashset.values():
            res.append(v)
        return res