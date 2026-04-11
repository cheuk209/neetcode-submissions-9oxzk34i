import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATORS = (
            '+',
            '-',
            '*',
            '/',
        )
        stack = []
        for token in tokens:
            if token not in OPERATORS:
                print('hello')
                stack.append(token)
            elif token in OPERATORS:
                second_expression = int(stack.pop())
                first_expression = int(stack.pop())
                if token == "+":
                    final_expression = first_expression + second_expression
                elif token == "-":
                    final_expression = first_expression - second_expression
                elif token == "*":
                    final_expression = first_expression * second_expression
                elif token == "/":
                    final_expression = first_expression / second_expression
                stack.append(final_expression)
 
        return int(stack[-1])
            