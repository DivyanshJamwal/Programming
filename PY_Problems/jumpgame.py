def canJump(nums):
    max_reachable = 0
    for i, num in enumerate(nums):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + num)
    return True

# Example usage:
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(canJump(nums))  # Output: True