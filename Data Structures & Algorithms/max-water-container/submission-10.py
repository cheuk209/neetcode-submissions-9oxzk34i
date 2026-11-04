class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_container = 0
        while l < r:
            current_container_height = min(heights[l], heights[r])
            max_container = max(max_container, current_container_height * (r - l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_container
