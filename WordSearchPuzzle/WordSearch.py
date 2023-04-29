import tkinter as tk
import os
import tkinter.font as tkFont
from os import listdir, getcwd
from random import choice, shuffle
from functools import partial



class WordBoard:

    def __init__(self, size=16, color="yellow", file_name="words.txt", words=None):

        assert size > 3, "Size must be greater than 3"

        root = tk.Tk()
        root.title("Word Search")
        root.resizable(width=False, height=False)

        self._word_grid = tk.Frame(root)
        self._word_list = tk.Frame(root)
        self._menu = tk.Frame(root)

        self._solution_shown = False
        self._size = size
        self._color = color

        # If file_name is not present in the current directory, the
        # New Words button will be disabled.
        new_words_button = tk.DISABLED
        if file_name in listdir(getcwd()):
            new_words_button = tk.NORMAL
            with open(file_name, mode="r") as f:
                self._wordstxt = filter(None, f.read().split("\n"))
                self._wordstxt = list(
                    filter(lambda x: len(x) < self._size - 3, self._wordstxt)
                )
        elif words is None:
            raise FileNotFoundError(
                f"""{file_name} not present in the current directory. {file_name}
                                    Add words manually in new words to start the game."""
            )

        # Buttons that have been pushed
        self._pushed = set()

        self._words = words
        if self._words is None:
            self._choose_random_words()
        else:
            self._words = list(set(map(str.upper, self._words)))

        # Create empty SIZExSIZE grid of buttons
        self._buttons = []
        for i in range(self._size):
            row = []
            for j in range(self._size):
                row.append(
                    tk.Button(
                        self._word_grid, padx=5, command=partial(self._pressed, i, j)
                    )
                )
                row[-1].grid(row=i, column=j, sticky="ew")
            self._buttons.append(row)

        # Menu Buttons at the top right of the GUI
        # Menu Label
        tk.Label(self._menu, text="Menu", pady=5, font=tkFont.Font(weight="bold")).grid(
            row=0, column=0, columnspan=2, sticky="ew"
        )
        # "New Words" Button
        tk.Button(
            self._menu,
            text="New Words",
            padx=1,
            pady=2,
            state=new_words_button,
            command=self._select_new,
        ).grid(row=1, column=0, sticky="ew")
      
        # "Solution" Button
        tk.Button(
            self._menu, text="Solution", padx=1, pady=2, command=self._solution
        ).grid(row=2, column=0, sticky="ew")
        # "Reshuffle" Button
        tk.Button(
            self._menu, text="Reshuffle", padx=1, pady=2, command=self._reshuffle
        ).grid(row=3, column=0, sticky="ew")

        self._labels = {}
        self._word_search = None
        self._create_labels()
        self._reshuffle()

        self._word_grid.pack(side=tk.LEFT)
        self._menu.pack(side=tk.TOP, pady=self._size)
        self._word_list.pack(side=tk.TOP, padx=40, pady=20)

        tk.mainloop()

    def _create_labels(self):
        """
        Creates/changes the word labels on the right side of the GUI.
        """
        for label in self._labels.values():
            label.destroy()
        self._labels.clear()
        self._labels = {
            "Words": tk.Label(
                self._word_list, text="Words", pady=5, font=tkFont.Font(weight="bold")
            )
        }
        self._labels["Words"].grid(row=2, column=0, columnspan=2)
        for i, word in enumerate(sorted(self._words)):
            self._labels[word] = tk.Label(self._word_list, text=word, anchor="w")
            self._labels[word].grid(
                row=(i // 2) + (i % 1) + 3, column=i % 2, sticky="W"
            )

    def _choose_random_words(self):

        self._words = set()
        for _ in range(choice(range(self._size // 3, self._size))):
            self._words.add(choice(self._wordstxt).upper())
        self._words = list(self._words)

    def _pressed(self, row, col):

        if self._buttons[row][col].cget("bg") == self._color:
            self._buttons[row][col].configure(bg="SystemButtonFace")
            self._pushed.remove((self._buttons[row][col].cget("text"), col, row))
        else:
            self._buttons[row][col].configure(bg=self._color)
            self._pushed.add((self._buttons[row][col].cget("text"), col, row))
            for word, coords in self._word_search.solutions.items():
                if coords & self._pushed == coords:
                    for _, col, row in coords:
                        self._buttons[row][col].configure(state=tk.DISABLED)
                    self._labels[word].configure(bg=self._color)

    def _solution(self):

        if self._solution_shown:
            bg = "SystemButtonFace"
            state = tk.NORMAL
            self._pushed.clear()
        else:
            bg = self._color
            state = tk.DISABLED

        self._solution_shown = not self._solution_shown
        for word, coords in self._word_search.solutions.items():
            self._labels[word].configure(bg=bg)
            for _, col, row in coords:
                self._buttons[row][col].configure(state=state, bg=bg)

    def _reshuffle(self):

        if self._solution_shown:
            self._solution_shown = not self._solution_shown
        self._word_search = WordSearch(self._size, self._words)
        self._pushed.clear()

        for i in range(self._size):
            for j in range(self._size):
                self._buttons[i][j].configure(
                    text=self._word_search.board[i][j],
                    bg="SystemButtonFace",
                    state=tk.NORMAL,
                )

        for label in self._labels.values():
            label.configure(bg="SystemButtonFace")

    def _select_new(self):
        """
        Command for the "New Words" button. Chooses a new randoms set of
        words from the file_name file and fills up the board with the new
        words and displays it in the GUI.
        """
        self._choose_random_words()
        self._reshuffle()
        self._create_labels()



class WordSearch:
    def __init__(self, size, words):

        self._size = size
        self._words = list(set(map(str.upper, words)))

        assert (
            self._size - max(map(len, self._words)) > 2
        ), f"Board Size {self._size} is too small."

        shuffle(self._words)
        self.board = [[None for _ in range(self._size)] for _ in range(self._size)]

        self.solutions = {}

        check = False
        while not check:
            self._init_board()
            check = self._fill_with_words()

        self._fill_board()

    def _get_orientation(self, word_len):

        starty = startx = 0
        endy = endx = self._size

        orient = choice(range(0, 4))

        if orient == 0:  # Horizontal
            ox = 1
            oy = 0
            endx = self._size - word_len  # board columns - word_len
        elif orient == 1:  # Vertical Down
            ox = 0
            oy = 1
            endy = self._size - word_len  # board rows - word_len
        elif orient == 2:  # Upward Diagonal
            ox = 1
            oy = -1
            starty = word_len
            endx = self._size - word_len  # board columns - word_len
        elif orient == 3:  # Downward Diagonal
            ox = 1
            oy = 1
            endy = self._size - word_len
            endx = self._size - word_len  # board columns - word_len

        x = choice(range(startx, endx))
        y = choice(range(starty, endy))

        return x, y, ox, oy

    def _check_board(self, word, x, y, ox, oy):

        for i, letter in enumerate(word):
            x_coord = x + i * ox
            y_coord = y + i * oy
            if self.board[y_coord][x_coord] != letter and self.board[y_coord][x_coord]:
                return False

        return True

    def _add_word(self, word):

        x, y, ox, oy = self._get_orientation(len(word))

        count = 0
        while not self._check_board(word, x, y, ox, oy):
            x, y, ox, oy = self._get_orientation(len(word))
            count += 1
            # Check for infinite loop
            if count > 20000:
                return False

        self.solutions[word] = set()
        for i, letter in enumerate(word):
            x_coord = x + i * ox
            y_coord = y + i * oy
            self.board[y_coord][x_coord] = letter
            self.solutions[word].add((letter, x_coord, y_coord))

        return True

    def _fill_board(self):
        for i in range(self._size):
            for j in range(self._size):
                if not self.board[i][j]:
                    self.board[i][j] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def _init_board(self):

        for i in range(self._size):
            for j in range(self._size):
                self.board[i][j] = None

    def _fill_with_words(self):
        for word in self._words:
            check = self._add_word(word)
            if not check:
                return False

        return True

    def __len__(self):

        return self._size

    def __str__(self):
        return "\n".join([" ".join(row) for row in self.board])


def main():
    print("Welcome to the WordSearch creator!")
    print("This program creates Word Search Puzzles.")
    print()
    print("The menu has four buttons which perform the following functions:")
    print("\t1. New Words: Generate a new random set of words to search for.")
    print(
        "\tA text file containing words separated by newline characters called words.txt must be present in the current directory in order for this feature to work."
    )
    print(
        "\t2. Solution: Show the location of each word on the Word Search board. Toggles on/off"
    )
    print(
        "\t3. Reshuffle: Creates a new Word Search grid with the same words in new positions"
    )
    print()
    print(
        'Click the buttons on the grid corresponding to the found word to "find" words'
    )
    print()
    print("Defaults ->", "Size: 16x16,", "Color: Yellow")
    print(
        "If you'd like to change the defaults, enter the desired values in the prompts below:"
    )
    size = input("Size (Enter for Default): ")
    print(
        "Check valid color options here: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter"
    )
    print("Entering an invalid color option will break the program.")
    color = input("Color (Enter for Default): ")
    print(
        "If you'd like to add a custom word list to replace words.txt, place the file in this directory and enter the file name below. Make sure words are separated by newline characters: "
    )
    file_name = input("New Words File Name (Enter for Default): ")
    print(
        "If you'd like to create a customized Word Search, enter the words below, one at a time:"
    )

    check = "a"
    words = []
    while check:
        check = input("Next Word (Enter the words): ")
        words.append(check)

    size = int(size) if size else 16
    color = color if color else "yellow"
    file_name = file_name if file_name else "words.txt"
    words = words[:-1] if words[:-1] else None

    WordBoard(size=size, color=color, file_name=file_name, words=words)


if __name__ == "__main__":
    main()
