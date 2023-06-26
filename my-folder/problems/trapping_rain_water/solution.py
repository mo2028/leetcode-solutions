class Solution:
    def trap(self, height: List[int]) -> int:
        # inint edge case
        if not height:
            return 0

        # init l and r
        l, r = 0, len(height) - 1

        # inint leftMax, rightMax
        # leftMax, rightMax = 0, <- wrong
        leftMax, rightMax = height[l], height[r]
        # init result
        res = 0

        while l < r:
            if leftMax < rightMax:

                l += 1
                # update leftMax
                leftMax = max(height[l], leftMax)
                # update result 
                res += leftMax - height[l]
            
            else:
                r -= 1
                # update rightMax
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
        return res