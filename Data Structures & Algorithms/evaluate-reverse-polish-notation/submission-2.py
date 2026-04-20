class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for n in tokens:
            if n not in operators:
                stack.append(n)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                val = str(int(eval(op2 + n + op1)))
                # print(val)
                stack.append(val)

        return int(stack.pop())
