class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            match c:
                case "+":
                    r = int(stack.pop())
                    l = int(stack.pop())
                    stack.append(str(l + r))
                case "-":
                    r = int(stack.pop())
                    l = int(stack.pop())
                    stack.append(str(l - r))
                case "*":
                    r = int(stack.pop())
                    l = int(stack.pop())
                    stack.append(str(l * r))
                case "/":
                    r = int(stack.pop())
                    l = int(stack.pop())
                    stack.append(str(int(l / r)))
                case _:
                    stack.append(c)
        return int(stack.pop())



                




