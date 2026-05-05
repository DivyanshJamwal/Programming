def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    # Initialize DP array
    dp = [1] * len(nums)

    # Fill DP array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in DP array
    return max(dp)

# Example usage
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Length of Longest Increasing Subsequence:", longest_increasing_subsequence(nums))