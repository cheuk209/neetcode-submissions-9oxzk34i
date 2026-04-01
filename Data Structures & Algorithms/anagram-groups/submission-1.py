class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        existing_ana = defaultdict(list)
        
        
        for word in strs:
            count = [0] * 26 # a ... z

            for character in word:
                count[ord(character) - ord("a")] += 1

            existing_ana[tuple(count)].append(word)
            print(existing_ana)
        return existing_ana.values()
            
