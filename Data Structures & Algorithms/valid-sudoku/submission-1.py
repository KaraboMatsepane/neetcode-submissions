class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)   # key: row number, value: set
        cols = collections.defaultdict(set)   # key: col number, value set
        grids = collections.defaultdict(set)  # key: grid index: (row // 3, col //3)

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                
                if (value in rows[row] or 
                    value in cols[col] or
                    value in grids[(row // 3, col // 3)]):

                    return False

                rows[row].add(value)
                cols[col].add(value)
                grids[(row // 3, col //3)].add(value)

        return True








        

        