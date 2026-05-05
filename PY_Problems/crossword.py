def can_place_word_horizontally(grid, word, row, col):
    if col + len(word) > len(grid[0]):
        return False
    for i in range(len(word)):
        if grid[row][col + i] not in ('-', word[i]):
            return False
    return True

def can_place_word_vertically(grid, word, row, col):
    if row + len(word) > len(grid):
        return False
    for i in range(len(word)):
        if grid[row + i][col] not in ('-', word[i]):
            return False
    return True

def place_word_horizontally(grid, word, row, col):
    original = []
    for i in range(len(word)):
        original.append(grid[row][col + i])
        grid[row][col + i] = word[i]
    return original

def place_word_vertically(grid, word, row, col):
    original = []
    for i in range(len(word)):
        original.append(grid[row + i][col])
        grid[row + i][col] = word[i]
    return original

def remove_word_horizontally(grid, original, row, col):
    for i in range(len(original)):
        grid[row][col + i] = original[i]

def remove_word_vertically(grid, original, row, col):
    for i in range(len(original)):
        grid[row + i][col] = original[i]

def solve_crossword(grid, words, index):
    if index == len(words):
        return True

    word = words[index]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if can_place_word_horizontally(grid, word, row, col):
                original = place_word_horizontally(grid, word, row, col)
                if solve_crossword(grid, words, index + 1):
                    return True
                remove_word_horizontally(grid, original, row, col)

            if can_place_word_vertically(grid, word, row, col):
                original = place_word_vertically(grid, word, row, col)
                if solve_crossword(grid, words, index + 1):
                    return True
                remove_word_vertically(grid, original, row, col)

    return False

def crossword_puzzle(grid, words):
    words = words.split(';')
    grid = [list(row) for row in grid]
    solve_crossword(grid, words, 0)