class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        otherValueMap = {}
        
        for i in range(len(nums)):
            value = target - nums[i]

            if value in otherValueMap:
                return [i, otherValueMap[value]]
            otherValueMap[nums[i]] = i

        

        
        
        



        