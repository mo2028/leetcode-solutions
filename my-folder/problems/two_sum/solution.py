class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        otherValueMap = {}
        for i in range(len(nums)):
            otherValue = target - nums[i]
            if otherValue in otherValueMap:
                return [otherValueMap[otherValue], i]
            otherValueMap[nums[i]] = i
        print(otherValueMap)
        return []




