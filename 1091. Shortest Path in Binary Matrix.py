# BFS for shortest path
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #n=number of row
        n = len(grid)
        #case if starting cell is block
        if grid[0][0]==1:
            return -1
        #case where single cell grid #number of visited cell=1
        if n==1:
            return 1
        #BFS over (row, col)
        #initialize queue with state
        q = deque([(0,0)])
        v = {(0,0)}
        #path length start at 0
        result = 0
        #process all node at current before moving
        while q:
            result+=1
            for _ in range(len(q)):
                current_row, current_col = q.popleft()
                #check if reached
                if current_row == n-1 and current_col == n-1:
                    return result
                #check all 8 direction
                for a,b in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    next_row, next_col = current_row+a, current_col+b
                    if 0<=next_row<n and 0<=next_col<n:                    
                            #if next move is 0, move
                            if grid[next_row][next_col]==0:
                                state = (next_row, next_col)
                                #check visited
                                if state not in v:
                                    q.append(state)
                                    v.add(state)            

        return -1
