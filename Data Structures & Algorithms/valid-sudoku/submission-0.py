from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashset = defaultdict(set)
        col_hashset = defaultdict(set)
        subgrid_hashset = defaultdict(set)

        for row_index, row in enumerate(board):
            for col_index, col_value in enumerate(row):
                subgrid_cooords = (row_index // 3, col_index // 3)
                if col_value == ".":
                    continue
                if col_value in row_hashset[row_index] or col_value in col_hashset[col_index] or col_value in subgrid_hashset[subgrid_cooords]:
                    return False
                else:
                    row_hashset[row_index].add(col_value) 
                    col_hashset[col_index].add(col_value)
                    subgrid_hashset[subgrid_cooords].add(col_value)
        return True