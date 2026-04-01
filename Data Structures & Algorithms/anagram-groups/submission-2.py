class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        result_list = []
        for str in strs:
            sorted_str = sorted(str)
            print(type(sorted_str))
            sorted_str = "".join(sorted_str)
            if sorted_str in hash_map:
                hash_map[sorted_str].append(str)
            else:
                hash_map[sorted_str] = [str]
        for k,v in hash_map.items():
            result_list.append(v)
        return result_list