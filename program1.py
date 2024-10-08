class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid or not grid[0]:
            return 0

        def dfs_iterative(x, y):
         
            stack = [(x, y)]
            
            while stack:
                i, j = stack.pop()
                
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 'L':
                    continue
                
                grid[i][j] = 'V'
                
               
                stack.append((i + 1, j))  # down
                stack.append((i - 1, j))  # up
                stack.append((i, j + 1))  # right
                stack.append((i, j - 1))  # left

        island_count = 0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':  
                    island_count += 1   
                    dfs_iterative(i, j) 
        
        return island_count