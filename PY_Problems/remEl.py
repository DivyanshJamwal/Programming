def removeElement(nums, val):
    """
    Removes all instances of `val` in-place and returns the new length.
    
    :param nums: List[int] - The input list of numbers.
    :param val: int - The value to remove.
    :return: int - The new length of the list after removal.
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Example usage:
if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    new_length = removeElement(nums, val)
    print(f"New length: {new_length}")
    print(f"Modified list: {nums[:new_length]}")