class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        lst = [[1],[1,1]]
        
        for i in range(1, numRows-1):
            lst2 = [1]
            for j in range(len(lst[i])-1):
                lst2.append(lst[i][j]+lst[i][j+1])
            lst2.append(1)
            lst.append(lst2)
        return lst
