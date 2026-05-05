def uniquePaths(m: int, n: int) -> int:
    # Create a 2D DP array with dimensions m x n
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # The bottom-right corner contains the result
    return dp[m - 1][n - 1]

# Example usage
if __name__ == "__main__":
    m, n = 3, 7
    print(f"Unique paths for a {m}x{n} grid: {uniquePaths(m, n)}")