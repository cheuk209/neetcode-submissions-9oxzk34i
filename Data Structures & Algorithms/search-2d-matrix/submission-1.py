class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                print("potentially!")
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid_point = (left + right) // 2
                    if row[mid_point] < target:
                        left = mid_point + 1
                    elif row[mid_point] > target:
                        right = mid_point - 1
                    else:
                        return True
            else:
                continue
        return False