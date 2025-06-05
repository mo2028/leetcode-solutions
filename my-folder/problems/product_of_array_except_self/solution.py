class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)

        product = 1
        # [1, 1, 2, 6]
        for i in range(1, len(nums)):
            left[i] = product * nums[i-1]
            product = left[i]
        print(left)

        # [24, 12, 4, 1]
        product = 1
        for i in range(len(nums)-2, -1, -1):
            right[i] = product * nums[i+1]
            product = right[i]
        
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] =  left[i] * right[i]
        
        return result




        




        