"""Problem:
	Unique Paths
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	How many possible unique paths are there?
	+---+---+---+---+
	| S |   |   |   |
	+---+---+---+---+
	|   |   |   |   |
	+---+---+---+---+
	|   |   |   | E |
	+---+---+---+---+
	Above is a 3 x 4 grid. How many possible unique paths are there?
"""

def unique_paths_count(m, n):
    """
    1. Define the objective function
		f(i, j) is the number of distinct ways to reach the i-th stair.
	2. Identify base cases
		f(1,1) = 1
		f(2,2) = 2
	3. Write down a recurrence relation for the optimized objective function
		f(i, j) = f(i-1, j) + f(i, j-1)
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(i, j)
    """
    dp = []
    for i in range(m):
        dp.append([0] * n)

    dp[0] = [1] * n
    for i in range(m):
        dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


# print(unique_paths_count(3, 4))


def uniquePathsWithObstacles(obstacleGrid):
        dp = []
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            dp.append([0]* n)
            
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i > 0:
                    dp[i][j] = dp[i-1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j-1]
                    
        return dp[m-1][n-1]


# print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))


def max_profit(grid):
    """
    Problem:
	Maximum Profit in a Grid
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	Each cell contains a coin the robot can collect.
	What is the maximum profit the robot can accumulate?
	+---+---+---+---+
	| S | 2 | 2 | 1 |
	+---+---+---+---+
	| 3 | 1 | 1 | 1 |
	+---+---+---+---+
	| 4 | 4 | 2 | E |
	+---+---+---+---+

    f(i, j) = P(i, j) + max(f(i-1, j), f(i, j-1))
    """
    dp = []
    m, n = len(grid), len(grid[0])
    for i in range(m):
        dp.append([0] *  n)
    
    # dp[0][0] = grid[0][0]

    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            elif j > 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]

    return dp[m-1][n-1]


grid = [
    [0, 2, 2, 50],
    [3, 1, 1, 100],
    [4, 4, 2, 0]]

# print(max_profit(grid))


def max_profit_path(grid):
    """
    Print the max profit path
    """
    m, n = len(grid), len(grid[0])
    dp = []
    from_path = []
    for i in range(m):
        dp.append([0] * n)
        from_path.append([0] * n)
    
    for i in range(m):
        for j in range(n):
            dp[i][j] = grid[i][j]
            if i > 0 and j > 0:
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] += dp[i-1][j]
            elif j > 0:
                dp[i][j] += dp[i][j-1]

            if dp[i-1][j] < dp[i][j-1]:
                from_path[i][j] = (i, j-1)
            else:
                from_path[i][j] = (i-1, j)

    path, i, j = [], m-1, n-1
    while i >= 0 and j >= 0:
        path.append((i, j))
        i, j = from_path[i][j]

    path.append((0,0))
    path.reverse()

    print(dp)
    return dp[m-1][n-1], path
    


print(max_profit_path(grid))
