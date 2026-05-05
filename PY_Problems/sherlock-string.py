from collections import Counter

def isValid(s):

    # Count the frequency of each character
    freq = Counter(s)
    freq_values = list(freq.values())

    # Count the frequency of frequencies
    freq_count = Counter(freq_values)

    if len(freq_count) == 1:
        # All characters have the same frequency
        return "YES"
    elif len(freq_count) == 2:
        # Two different frequencies
        freq_items = list(freq_count.items())
        # Check if one frequency occurs only once and is either 1 or can be reduced to match the other frequency
        if (freq_items[0][1] == 1 and (freq_items[0][0] == 1 or abs(freq_items[0][0] - freq_items[1][0]) == 1)) or \
           (freq_items[1][1] == 1 and (freq_items[1][0] == 1 or abs(freq_items[1][0] - freq_items[0][0]) == 1)):
            return "YES"
    return "NO"

# Input and output handling
if __name__ == "__main__":
    s = input().strip()
    print(isValid(s))