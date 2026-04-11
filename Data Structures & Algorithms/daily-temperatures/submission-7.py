class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        warm_stack = []

        for index, temp in enumerate(temperatures):
            if index == 0:
                warm_stack.append((index, temp))
                continue
            while warm_stack and temp > warm_stack[-1][1]:
                flag_index, flag_temp = warm_stack.pop()
                result[flag_index] = index - flag_index
            warm_stack.append((index, temp))
            print(warm_stack)
            
        return result