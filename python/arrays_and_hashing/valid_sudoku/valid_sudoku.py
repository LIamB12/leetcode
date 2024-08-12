class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validate_row(row):
            seen = set()
            for num in row:
                if num == ".":
                    continue

                if num in seen:
                    return False
                else:
                    seen.add(num)

            return True


        def validate_box(box):
            seen = set()
            for row in range(3):
                for col in range(3):
                    num = box[row][col]

                    if num == ".":
                        continue

                    if num in seen:
                        return False
                    else:
                        seen.add(num)

            return True

        
        for row in board:
            if not validate_row(row):
                return False

        transposed_board = [[board[col][row] for col in range(9)] for row in range(9)]
        for row in transposed_board:
            if not validate_row(row):
                return False

        for i in range(3):
            for j in range(3):
                box = [
                    board[(i * 3)][(j * 3):(j * 3 + 3)],
                    board[(i * 3 + 1)][(j * 3):(j * 3 + 3)],
                    board[(i * 3 + 2)][(j * 3):(j * 3 + 3)]
                ]

                if not validate_box(box):
                    return False

        return True


