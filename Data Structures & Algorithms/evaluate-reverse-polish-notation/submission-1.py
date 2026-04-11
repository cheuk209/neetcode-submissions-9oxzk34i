import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATORS = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        stack = []
        for token in tokens:
            if token not in OPERATORS:
                print('hello')
                stack.append(token)
            elif token in OPERATORS:
                second_expression = stack.pop()
                first_expression = stack.pop()
                final_expression = OPERATORS[token](int(first_expression), int(second_expression))
                stack.append(final_expression)
 
        return int(stack[-1])
            