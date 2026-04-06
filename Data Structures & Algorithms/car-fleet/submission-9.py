class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse = True)
        print(pairs)

        for (pos, spd) in pairs:
            remain = target - pos
            arrival = remain / spd

            if not stack or arrival > stack[-1]:
                stack.append(arrival)
        return len(stack)

