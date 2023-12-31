class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            middleRow = (top + bot) //  2

            if target > matrix[middleRow][-1]:
                top = middleRow + 1
            elif target < matrix[middleRow][0]:
                bot = middleRow - 1
            else:
                break

        if not(top <= bot):
            return False
        
        l, r = 0, COLS - 1

        while l <= r:

            middleElement = (l + r) // 2

            if target > matrix[middleRow][middleElement]:
                l = middleElement  +  1
            elif target < matrix[middleRow][middleElement]:
                r = middleElement  - 1
            else:
                return True
        
        return False

    
    
