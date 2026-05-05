def removeDuplicates(nums):
    if not nums:
        return 0

    # Pointer for the position of the unique element
    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1

# Example usage
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicates(nums)
    print(f"Array after removing duplicates: {nums[:k]}")
    print(f"Number of unique elements: {k}")