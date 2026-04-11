class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        warm_stack = []
        for i, temp in enumerate(temperatures):
            current_index = i + 1
            while current_index <= len(temperatures) - 1:
                print(temp, temperatures[current_index])
                if temperatures[current_index] > temp:
                    result[i] = current_index - i
                    break
                else:
                    current_index += 1
            
        return result