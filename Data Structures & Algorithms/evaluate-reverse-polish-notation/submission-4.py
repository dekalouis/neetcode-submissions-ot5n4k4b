class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens is None:
            return None
        stack = []

        for i in range(len(tokens)):
            # print(tokens[i])
            if tokens[i] in "*+-/":
                rightop = stack.pop()
                leftop = stack.pop()
                # print(f"r: {rightop}, l: {leftop}")
                if tokens[i] == "*":
                    # print(tokens[i])
                    stack.append(str(int(leftop) * int(rightop)))
                    # print(f"{rightop} {tokens[i]} {leftop} = {int(leftop) * int(rightop)}")
                elif tokens[i] == "+":
                    # print(tokens[i])
                    stack.append(str(int(leftop) + int(rightop)))
                    # print(f"{rightop} {tokens[i]} {leftop} = {int(leftop) + int(rightop)}")
                elif tokens[i] == "-":
                    # print(tokens[i])
                    stack.append(str(int(leftop) - int(rightop)))
                    # print(f"{rightop} {tokens[i]} {leftop} = {int(leftop) - int(rightop)}")
                elif tokens[i] == "/":
                    # print(tokens[i])
                    stack.append(str(int(int(leftop) / int(rightop))))
                    # print(f"{rightop} {tokens[i]} {leftop} = {int(leftop) / int(rightop)}")
            else:
                stack.append(tokens[i])
     
            # print(stack)
        return int(stack[0])
