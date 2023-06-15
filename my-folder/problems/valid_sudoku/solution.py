class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # define three maps 
        # row -> set
        rows = defaultdict(set)
        # columns -> set
        cols = defaultdict(set)
        # square -> set
        sqrs = defaultdict(set)


        # iterate and check 
        # does range(n), go till n?

        for row in range(9):
            for col in range(9):

                # for sqr in range(3): <- dont need this
                    # continue if "." [case 1]
                if board[row][col] == ".":
                    continue   

                # check if dup. exists [case 2]
                # I had "if row in rows[row] or col in cols[col] or sqr in sqrs[row//3, col//3]:", which is wrong because it is not using the actual value in the board
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in sqrs[row//3, col//3]:
                    return False

                    # case[3]; gotta add into the set if it does not exist in the dict
                    # I did rows.add(board[row][col]), which is wrong because I'm not giving the key like 
                    # rows[row]
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                sqrs[row//3, col//3].add(board[row][col])



        return True
                    

