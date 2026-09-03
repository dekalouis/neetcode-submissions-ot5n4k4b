class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #initialize stack, then create pairs, sorting in reverse a ZIP:
        # position = [4, 1, 0, 7]
        # speed =    [2, 2, 1, 1]
        # zip(position, speed) → [(4,2), (1,2), (0,1), (7,1)] 
        # loop destructured pos spd in those tuple pairs
        # in it, you want to find the remaining hour, (target-pos) and also the arrival time (rem)/spd
        # if stack is empty OR the arrivaltime is > last entry of the stack, append arrival to stack
        # otherwise do nothing and return the len of stack

        stack = []
        pairs = sorted(zip(position, speed), reverse=True)

        for pos, spd in pairs: 
            remain = target - pos
            arrival_time = remain / spd
            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
        return len(stack)