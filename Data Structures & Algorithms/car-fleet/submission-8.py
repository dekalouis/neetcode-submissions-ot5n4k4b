class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse = True)

        for p, s in pairs:
            remain = target - p
            arrival = remain / s

            if not stack or arrival > stack[-1]:
                stack.append(arrival)

        return len(stack)