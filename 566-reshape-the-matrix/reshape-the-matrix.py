class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        result=[]
        arr=[]
        for row in mat:
            for x in row:
                arr.append(x)
        k=0
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(arr[k])
                k+=1
            result.append(row)
        return result

        