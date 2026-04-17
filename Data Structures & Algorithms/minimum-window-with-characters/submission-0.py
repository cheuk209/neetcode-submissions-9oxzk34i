class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_hash = defaultdict(int)
        s_hash = defaultdict(int)
        result_str = []
        for char in t:
            t_hash[char] += 1
        
        have = 0
        need = len(t_hash)
        l = 0
        for r in range(len(s)):
            s_hash[s[r]] += 1
            if s_hash[s[r]] == t_hash[s[r]]:
                have += 1
            if have == need:
                while have == need:
                    result_str.append(s[l:r+1])
                    s_hash[s[l]] -= 1
                    print("what is l?", l)
                    if s_hash[s[l]] < t_hash[s[l]]:
                        have += -1
                    l += 1
        return min(result_str, key=len) if result_str else ""
