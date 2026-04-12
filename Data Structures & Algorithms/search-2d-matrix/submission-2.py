class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """
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
        """
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid_point = (left + right) // 2
            mid_row = matrix[mid_point]
            if mid_row[0] <= target and target <= mid_row[-1]:
                left_element = 0
                right_element = len(mid_row) - 1
                while left_element <= right_element:
                    mid_point = (left_element + right_element) // 2
                    if mid_row[mid_point] < target:
                        left_element = mid_point + 1
                    elif mid_row[mid_point] > target:
                        right_element = mid_point - 1
                    else:
                        return True
                return False
            elif target < mid_row[0]:
                right = mid_point - 1
            elif target > mid_row[-1]:
                left = mid_point + 1
        return False