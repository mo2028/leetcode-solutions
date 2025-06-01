class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = {}
        tCount = {}
        for n in s:
            sCount[n] = sCount.get(n,0) + 1

        for n in t:
            tCount[n] = tCount.get(n,0) + 1

        for n in s:
            if tCount.get(n,0) != sCount.get(n,0):
                return False
        return True
        
            