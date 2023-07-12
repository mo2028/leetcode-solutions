class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init a stack, a list 
        stk = []

        # inter through the list
        for tkn in tokens:
            # different cases
            if tkn == "+":
                stk.append(stk.pop() + stk.pop())
            elif tkn == "-":
                a, b = stk.pop(), stk.pop()
                stk.append(b-a)
            elif tkn == "*":
                stk.append(stk.pop() * stk.pop())
            elif tkn == "/":
                a, b = stk.pop(), stk.pop()
                stk.append(int(b/a))
            else:
                # TypeError: can't multiply sequence by non-int of type 'str'
                # stk.append(stk.pop() * stk.pop())
                # tkn was not being converted to an int from a char
                stk.append(int(tkn))

        return stk[0]
