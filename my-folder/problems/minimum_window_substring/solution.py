class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        res, resLen = [-1,-1], float('inf')
        l = 0
        window = {}
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                # time to shrink it 
                window[s[l]] = window.get(s[l],0) - 1
                # if its not the in the window but it is in t
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1 
        l, r = res
        return s[l: r+1] if resLen is not float('inf') else ""
            
            
        
        