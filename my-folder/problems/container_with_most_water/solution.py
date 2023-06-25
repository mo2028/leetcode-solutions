class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1 init left and right pointer
        left = 0
        right = len(height) -1

        maxArea = -1
        # 3 while loop to go throught all the values
        while left < right:
            # 2 calculate area
            # I had "area = max(height[left], height[right]) * (right - left)", which is wrong because it should be min
            area = min(height[left], height[right]) * (right - left)
            # 4 if statement for updating left 
            if height[left] < height[right]:
                left += 1
            # 5 if statement for updating right 
            else:
                right -= 1
            # max area
            maxArea = max(maxArea, area)

        return maxArea



        








       