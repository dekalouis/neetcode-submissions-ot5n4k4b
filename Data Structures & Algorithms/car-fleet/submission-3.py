class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse=True)

        for (pos, spd) in pairs:
            remaining = target - pos
            arrival = remaining / spd

            if not stack or arrival > stack[-1]:
                stack.append(arrival)

        return len(stack)