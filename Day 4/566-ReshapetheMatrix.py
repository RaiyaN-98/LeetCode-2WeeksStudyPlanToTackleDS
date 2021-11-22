class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if col*row != r*c:
            return mat
        lst = []
        lst2 = []
        for x in mat:
            for y in x:
                lst2.append(y)
                if len(lst2) == c:
                    lst.append(lst2)
                    lst2 = []
        return lst
                
