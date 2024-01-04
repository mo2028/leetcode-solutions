class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            k = (l+r)// 2

            # check if target is the mid
            if target == nums[k]:
                return k

            if nums[l] <= nums[k]: 
                if target > nums[k] or target < nums[l]:
                    l = k + 1
                else:
                    r = k - 1
            else:
                if target < nums[k] or target > nums[r]:
                    r = k - 1
                else:
                    l = k + 1


        return -1




