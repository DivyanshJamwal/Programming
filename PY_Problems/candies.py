def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]

# Example usage:
candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = kidsWithCandies(candies, extraCandies)
print(result)  # Output: [True, True, True, False, True]