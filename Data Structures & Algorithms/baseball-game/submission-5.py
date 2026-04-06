class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result_int = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                try:
                    stack.append(int(stack[-1]) + int(stack[-2]))
                except:
                    pass
                continue
            elif operations[i] == "C":
                stack.pop()
                continue
            elif operations[i] == "D":
                double_score = int(stack[-1]) * 2
                stack.append(double_score)
                continue
            stack.append(int(operations[i]))
        
        print(stack)
        for num in stack:

            result_int += int(num)

        return result_int