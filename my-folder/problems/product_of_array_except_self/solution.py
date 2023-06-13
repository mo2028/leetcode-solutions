class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init result array "res"
        res = [1]*len(nums)

        prefix = 1
        # foward pass but itself
        for i in range(0, len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        #backward pass by itself
        # I had "for i in range(len(nums)-1, -1):"", which does not have the third argument 
        # so it was a inifnite loop. need to put -1 to be able to go backwards 
        for i in range(len(nums)-1, -1, -1):
            # here, I had res[i]= postfix, this is wrong because it is most making use of the 
            # result that is already in the res array, and it is overwriting 
            res[i]= res[i] * postfix
            postfix = postfix * nums[i]
            

        return res