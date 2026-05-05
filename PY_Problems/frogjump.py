def frog_jump(n, heights):
    dp = [-1] * n

    def min_energy(step):
        if step == 0:
            return 0

        if dp[step] != -1:
            return dp[step]

        one_step = min_energy(step - 1) + abs(heights[step] - heights[step - 1])

        two_step = float('inf')
        if step > 1:
            two_step = min_energy(step - 2) + abs(heights[step] - heights[step - 2])

        dp[step] = min(one_step, two_step)
        return dp[step]

    return min_energy(n - 1)

# Example usage
if __name__ == "__main__":
    heights = [10, 30, 40, 20]
    n = len(heights)
    print(frog_jump(n, heights))  # Output: 30