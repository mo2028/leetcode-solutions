class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # init global stk
        stk = []
        # init global res
        res = []

        # openCount = 0
        # closedCount = 0

        # define backTrack function
        # make sure all the params match to what you use in the def
        def backTrack(openCount, closedCount):

            # base case is if leftCount == rightCount == n
            if openCount == closedCount == n:
                # cannot just do this res.append(stk)
                
                # rememeber "".join(stk)
                res.append("".join(stk))
                return

            #condition to add leftParan
            if openCount < n:
                stk.append("(")
                backTrack(openCount+1, closedCount)
                stk.pop()
            
            if closedCount < openCount:
                stk.append(")")
                backTrack(openCount, closedCount+1)
                stk.pop()


        backTrack(0, 0)
        return res



                
            












        