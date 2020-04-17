#Given a m x n grid filled with non-negative numbers, 
#find a path from top left to bottom right which minimizes 
#the sum of all numbers along its path.
# Ref: https://leetcode.com/problems/minimum-path-sum/

# DP relation: dp(i,j) = grid(i,j) + min(dp(i-1, j), dp(i, j-1))
#  

def minPathSum(grid: List[List[int]]) -> int:
        
        if not grid or len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        #initializing dp grid
        dp = [ [0] * cols for row in grid]
        
        for i in range(rows):
            for j in range(cols):
                
                val = grid[i][j] #default value for every cell
                
                if i == 0 and j > 0: #first row fill
                    val += dp[i][j-1]
                elif j == 0 and i > 0: #first col fill
                    val += dp[i-1][j]
                else:
                    val += min(dp[i][j-1], dp[i-1][j])
                dp[i][j] = val
            
        return dp[rows-1][cols-1] #the minimum value is find at the bottom right position