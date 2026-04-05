class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in board]
        cols = [set() for _ in board]
        boxes = [set() for _ in board]

        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]
                box_id = row//3 * 3 + col//3
                if value == ".":
                    continue
                if value in rows[row] or value in cols[col] or value in boxes[box_id]:
                    return False
                else:
                    rows[row].add(value)
                    cols[col].add(value)
                    boxes[box_id].add(value)

        return True