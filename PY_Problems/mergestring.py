def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    
    # Append the remaining characters from either string
    if i < len(word1):
        merged.append(word1[i:])
    if j < len(word2):
        merged.append(word2[j:])
    
    return ''.join(merged)

# Example usage
if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    print(mergeAlternately(word1, word2))  # Output: "apbqcr"