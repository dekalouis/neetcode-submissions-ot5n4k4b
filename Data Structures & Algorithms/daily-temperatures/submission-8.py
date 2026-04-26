class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initiate res with arrays filled with 0 at the length of the temps
        # make a stack that will store temp, idx
        # then for idx, temp in the enumerate of temperatures, 
        # and inside, while stack exists and temp > stack[-1][0]
        # create stackT, stackIdx from the pop value of stack
        # and res[stackidx] = i - stackidx, then
        # outside loop, append tuple of temp, idx to stack
        # return res

        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append((temp, idx))
        return res