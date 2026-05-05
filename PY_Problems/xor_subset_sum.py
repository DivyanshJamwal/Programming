def subsetXORSum(nums):
    def dfs(index, current_xor):
        if index == len(nums):
            return current_xor
        return dfs(index + 1, current_xor) + dfs(index + 1, current_xor ^ nums[index])
    
    return dfs(0, 0)