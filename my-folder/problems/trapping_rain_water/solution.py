class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftM = height[l]
        rightM = height[r]
        res = 0
        while l < r:
            if leftM < rightM:
                    l+=1
                    leftM = max(leftM, height[l])
                    res += leftM - height[l]
            else: 
                r-=1
                rightM = max(rightM, height[r])
                res += rightM - height[r]
        return res

            
