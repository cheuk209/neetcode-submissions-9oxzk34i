class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area_stack = []
        processed_area = []
        heights.append(0)
        for index, height in enumerate(heights):
            if len(area_stack) == 0:
                area_stack.append((index, height))
                continue
            if height >= area_stack[-1][1]:
                area_stack.append((index,height))
            else:
                while area_stack and height < area_stack[-1][1]:
                    prev_index, prev_height = area_stack.pop()
                    right_boundary = index
                    if len(area_stack) == 0:
                        left_boundary = -1
                    else:
                        left_boundary = area_stack[-1][0]
                    area_to_process = (right_boundary - left_boundary - 1) * prev_height
                    processed_area.append(area_to_process)
                area_stack.append((index, height))

        if len(processed_area) == 0:
            return 0
        return max(processed_area)
        