class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. init left and right pointers
        l, r = 0, len(numbers)-1

        # 2. big driver loop
        while l < r:

            tot = numbers[l] + numbers[r]

            # if statements to update the l and r pointers
            if tot  < target:
                l += 1
            elif tot > target:
                r -= 1
            else:
                return [l+1, r+1]
                
            







