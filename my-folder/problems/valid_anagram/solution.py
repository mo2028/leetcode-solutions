class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = {}
        tCount = {}
        
        for i in range(len(s)):
            sCount[s[i]]  = sCount.get(s[i], 0) + 1
            tCount[t[i]]  = tCount.get(t[i], 0) + 1
            
        
        for char in s:
            if sCount[char] != tCount.get(char, 0):
                return False
            
        return True