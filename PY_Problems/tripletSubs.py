def increasingTriplet(nums):
    first = second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

# Example usage
nums = [1, 2, 3, 4, 5]
print(increasingTriplet(nums))  # Output: True