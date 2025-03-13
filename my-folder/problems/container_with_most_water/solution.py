class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        # print(l, r)
        maxArea = 0
        while l < r:
            # print(l)
            # print(height[l], height[r])
            if height[l] <= height[r]:
                maxArea = max(maxArea, (r-l) * height[l])
                l+=1
                
            elif height[l] > height[r]:
                maxArea = max(maxArea, (r-l) * height[r])
                r-=1
                
            print(height[l], height[r])
            print(maxArea)
        return maxArea



        