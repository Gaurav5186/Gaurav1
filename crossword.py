class Crossword:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.clues = {}

    def add_word(self, word, row, col, direction):
        if direction == 'across':
            for i, letter in enumerate(word):
                self.grid[row][col + i] = letter
        elif direction == 'down':
            for i, letter in enumerate(word):
                self.grid[row + i][col] = letter
        else:
            raise ValueError("Invalid direction. Use 'across' or 'down'.")

        self.clues[(row, col, direction)] = f"{word}: {direction}"

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def display_clues(self):
        for clue in self.clues.values():
            print(clue)

def main():
    crossword = Crossword(size=5)

    crossword.add_word("hello", 1, 1, 'across')
    crossword.add_word("world", 2, 1, 'down')

    print("Crossword Grid:")
    crossword.display()

    print("\nClues:")
    crossword.display_clues()

if __name__ == "__main__":
    main()
