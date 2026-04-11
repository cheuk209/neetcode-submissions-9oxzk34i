class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left, max_right = 0, 0
        water_volume = 0
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                print("water volume will add at index ", left, max_left - height[left])
                water_volume +=  max_left - height[left]
                left += 1
            elif max_right < max_left:
                print("water volume will add at index ", right ,max_right - height[right])
                water_volume += max_right - height[right]
                right += -1
            else:
                print("water volume will add at index", left, right,  max_left - height[left], max_right - height[right])
                water_volume +=  max_left - height[left]
                water_volume +=  max_right - height[right]
                left += 1
                right += -1
        if left == right:
            print("what is left, right", left, right)
            print(min(max_left, max_right) - height[left])
            if min(max_left, max_right) > height[left]:
                water_volume += min(max_left, max_right) - height[left]
        return water_volume 