class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_temperatures = [0] * len(temperatures)
        mono_stack = []
        for index, temp in enumerate(temperatures):
            if len(mono_stack) == 0:
                mono_stack.append((index, temp))
                continue
            if temp <= mono_stack[-1][1]:
                mono_stack.append((index, temp))
            else:
                while mono_stack and temp > mono_stack[-1][1]:
                    prev_index, prev_temp = mono_stack.pop()
                    result_temperatures[prev_index] = (index - prev_index)
                mono_stack.append((index, temp))

        return result_temperatures
