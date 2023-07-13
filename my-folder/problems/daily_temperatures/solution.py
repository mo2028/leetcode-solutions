class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init stack, which is a stack of tuple (index, number)
        stk = [] 
        # init res array of zeros
        res = [0] * len(temperatures)

        # enumerat through the temperatures
        for i, t in enumerate(temperatures):
            # while loop
            # why? to 
            # had while stk and t > stk.top(), and list does not have top()
            # had to do stk[-1] to look at the last element, aka top()
            while stk and t > stk[-1][1]:
                index, topTemp = stk.pop()
                # i>index; had index - i
                res[index] = i - index
            # had stk.append(i, t), which is wrong because append is given two arguments and not a tuple
            # keep appending if stack is emply or t is <= top of the stack
            stk.append((i, t))
        return res


            









