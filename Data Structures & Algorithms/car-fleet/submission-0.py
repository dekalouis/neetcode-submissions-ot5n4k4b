class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = sorted(zip(position, speed), reverse=True)

        for (pos, spd) in pairs:
            remaining = target - pos
            arrival_time = remaining / spd
            # arrival.append(arrival_time)

            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
            else:
                continue

            print(arrival_time)
        
        # print(arrival)
        return len(stack)

