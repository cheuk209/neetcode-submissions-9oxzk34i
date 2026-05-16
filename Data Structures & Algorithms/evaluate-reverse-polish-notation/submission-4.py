class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in hashset:
                stack.append(token)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                print(x)
                print(y)
                if token == "+":
                    res = x + y
                elif token == "-":
                    res = x - y
                elif token == "*":
                    res = x * y
                elif token == "/":
                    res = x / y
                stack.append(res)
        return int(stack[-1])