class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # when pushed, want to maintain the min at the top of minStack
        # compare the top of stack and minStack and push update or not the min        accordingly
        # 
        # [-2, 0, -3]
        # [-2, -2, -3]
        # AttributeError: 'list' object has no attribute 'push'
        

        if  len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        

    def pop(self) -> None:
        print(self.stack)
        self.stack.pop()
        print(self.stack)
        print( self.minStack)
        self.minStack.pop()
        print( self.minStack)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]



        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()