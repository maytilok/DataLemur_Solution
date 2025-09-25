#need to use BFD in shortest path in unweight graph
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #m=number of row, n=number of column
        m, n = len(grid), len(grid[0])

        #case when single cell grid
        if m == 1 and n == 1:
            return 0  # Already at destination

        #case where we have enogh elimination k to go straight right and then down (or down then right), which would be the shortest path
        if k>(m-1)+(n-1):
          return (m-1)+(n-1) #number of step to straight right and then down (or down then right)
            
        #BFS over (row, col, elim) elim<k

        #check if starting cell is obstacle
        initial_k = k if grid[0][0] == 0 else k - 1 #if first cell is obstacle, start when elmination already use 1 = k-1
        if initial_k < 0:
            return -1  # Can't even start
        
        #initialize queue with staring state
        q = deque([(0,0,initial_k)])
        #visited to track visited states
        visited = {(0,0,initial_k)}
        #track current steps
        result = 0

        #Level-by-Level BFS Travel in grid (Find shortest path)

        #process all nodes at the current level before moving to next level
        while q:
            result+=1
            for _ in range(len(q)):
                current_row, current_col, remain_k = q.popleft() #moving to next level (next left node in tree or graph)
            
            #exploring neighbor Check all four directions (up, down, right, left) from the current position.
                for a, b in [[0,-1], [0,1], [-1,0], [1,0]]:
                    next_row, next_col = current_row+a, current_col+b

                    #Boundary and goal check
                    
                    #check new postition is within bound
                    if 0 <= next_row < m and 0 <= next_col <n: #still within boundary
                        # if reach destinationm return the current step (result), reach (m-1, n-1)
                        if next_row == m-1 and next_col == n-1:
                            return result

                        #if empty cell (0), move without using elimination 
                        if grid[next_row][next_col] == 0:
                            state = (next_row, next_col, remain_k) #not use remain so return same remain
                            # check ((next_row, next_col) is not in visited (avoid repeated node)
                            if state not in visited:
                                q.append(state)
                                visited.add(state)
                        
                        #if obstacle cell(1), if remain_k < k, move with using elimanation, else return to current state
                        elif grid[next_row][next_col] == 1 and remain_k>0:
                            state  = (next_row, next_col, remain_k-1)
                            # check ((next_row, next_col) is not in visited (avoid repeated node)
                            if state not in visited:
                                q.append(state)
                                visited.add(state)  
        #no path found
        return -1                               

             


                




        
