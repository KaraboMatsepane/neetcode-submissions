class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Step 1:
        # Input: soduku board
        # Output: True if the board is valid, otherwise false
        # constraints

        # Step 2:
        # example: 

        # step 3:
        # what is repeateadly checked: for each number, are there duplicates on the same row, column or 3 x 3 block
        # data structure: hashset

        # Step 4:

        # loop through each row (inner lists), convert each to a set, and check if their length is 9
        # rotate column 90 degrees to clockwise, and do it again to check columns
        # we will continue with grids after

        n = len(board)

        for i in range(n):
            row_numbers = []
            col_numbers = []

            for j in range(n):
                row_element = board[i][j]
                col_element = board[j][i]

                if row_element.isnumeric():
                    row_numbers.append(row_element)

                if col_element.isnumeric():
                    col_numbers.append(col_element)
                    

            if len(set(row_numbers)) != len(row_numbers) or len(set(col_numbers)) != len(col_numbers):
                return False



        for row in range(0, n, 3):

            for col in range(0, n, 3):
                grid_nums = []

                for grid_row in range(row, row + 3):
                    for grid_col in range(col, col + 3):
                        grid_element = board[grid_row][grid_col]
                        if grid_element.isnumeric():
                            grid_nums.append(grid_element)

                if len(set(grid_nums)) != len(grid_nums):
                    return False
        
        return True





        

        