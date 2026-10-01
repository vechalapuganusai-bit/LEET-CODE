class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n=len(grid)
        answer=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]>0:
                    answer+=1
        for i in range(n):
            answer+=max(grid[i])
        for j in range(n):
            column_max=0
            for i in range(n):
                column_max=max(column_max, grid[i][j])
            answer+=column_max
        return answer

        
        