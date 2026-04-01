class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        existing_ana = {}
        for word in strs:
            new_word = "".join(sorted(word))
            if new_word in existing_ana:
                existing_ana[new_word].append(word)
            else:
                existing_ana[new_word] = [word]
        result = []
        for k, v in existing_ana.items():
            result.append(v)
            
        return result