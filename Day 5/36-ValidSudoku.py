class Solution:
    def check(self, lst: List[List[str]]):
        for x in lst:
            lst2 = []
            for y in x:
                if y in lst2:
                    return False
                lst2.append(y)
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        squares = []
        for i in range(9):
            rows.append([])
            columns.append([])
            squares.append([])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] != "."):
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    m = 0
                    n = 0
                    if i < int(3): m = 0
                    elif i < int(6): m = 3
                    else: m = 6
                    if j < int(3): n = 0
                    elif j < int(6): n = 1
                    else: n = 2
                    squares[m+n].append(board[i][j])
        return self.check(rows) and self.check(columns) and self.check(squares)
