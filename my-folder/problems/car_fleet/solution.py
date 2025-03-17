class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [ (target-p)/s for p, s in sorted(zip(position, speed), reverse = True)]
        stack = []
        for eachTime in times:
            if not stack or eachTime > stack[-1]:
                stack.append(eachTime)
        # print(stack)
        return(len(stack))


        