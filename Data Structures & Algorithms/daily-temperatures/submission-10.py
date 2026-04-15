class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prev_temp_stack = []
        result = [0] * len(temperatures)
        if len(temperatures) == 0:
            return []
        if len(temperatures) == 1:
            return [0]
        for day, temp in enumerate(temperatures):
            if len(prev_temp_stack) == 0:
                prev_temp_stack.append((day, temp))
                continue
            
            if temp <= prev_temp_stack[-1][1]:
                prev_temp_stack.append((day, temp))
            
            else:
                print("what is temp", temp, "what is prev_temp", prev_temp_stack[-1][1])
                while prev_temp_stack and temp > prev_temp_stack[-1][1]:
                    prev_day, prev_temp = prev_temp_stack.pop()
                    result[prev_day] = (day - prev_day)
                prev_temp_stack.append((day, temp))
        return result
