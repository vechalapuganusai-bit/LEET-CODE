class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n=len(grid)
        area=0
        for i in range(n):
            for j in range(n):
                h=grid[i][j]
                if h>0:
                    area+=2
                    if i==0:
                        area+=h
                    else:
                        area+=max(0, h-grid[i-1][j])
                    if i==n-1:
                        area+=h
                    else:
                        area+=max(0, h-grid[i+1][j])
                    if j==0:
                        area+=h
                    else:
                        area+=max(0,h-grid[i][j-1])
                    if j==n-1:
                        area+=h
                    else:
                        area+=max(0, h-grid[i][j+1])
        return area        