#!/usr/bin/env python3
import random
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = max(1, int(width))
        self.height = max(1, int(height))
        max_mines = self.width * self.height - 1
        mines = int(mines)
        # Cap mines to a sane value (at least one non-mine cell)
        if mines < 0:
            mines = 0
        if mines > max_mines:
            mines = max_mines
        self.mines = set(random.sample(range(self.width * self.height), mines))
        self.field = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.revealed = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.total_cells = self.width * self.height
        self.mines_count = len(self.mines)
        self.to_reveal = self.total_cells - self.mines_count
        self.revealed_count = 0

    def print_board(self, reveal=False):
        clear_screen()
        # Column header
        header = '   ' + ' '.join(f'{i:2}' for i in range(self.width))
        print(header)
        for y in range(self.height):
            row = f'{y:2} '
            for x in range(self.width):
                idx = y * self.width + x
                if reveal or self.revealed[y][x]:
                    if idx in self.mines:
                        row += ' *'
                    else:
                        count = self.count_mines_nearby(x, y)
                        row += f' {count}' if count > 0 else '  '
                else:
                    row += ' .'
            print(row)

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Validate coordinates
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # treat as no-op (play() will inform user about bounds)
        idx = y * self.width + x
        if idx in self.mines:
            # Hit a mine
            return False

        # Iterative flood-fill to reveal connected empty area (avoid recursion)
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if self.revealed[cy][cx]:
                continue
            # If it's a mine, skip revealing it (shouldn't happen because we checked initial)
            if (cy * self.width + cx) in self.mines:
                continue
            self.revealed[cy][cx] = True
            self.revealed_count += 1
            # If this cell has no adjacent mines, reveal neighbors
            if self.count_mines_nearby(cx, cy) == 0:
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            # Do not add neighbor if it's a mine
                            if (ny * self.width + nx) not in self.mines:
                                stack.append((nx, ny))
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                raw_x = input("Enter x coordinate: ").strip()
                raw_y = input("Enter y coordinate: ").strip()
                if raw_x == '' or raw_y == '':
                    print("Please enter both coordinates.")
                    continue
                x = int(raw_x)
                y = int(raw_y)
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordinates out of bounds. x must be 0..{self.width-1}, y must be 0..{self.height-1}.")
                    continue
                ok = self.reveal(x, y)
                if not ok:
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                # Check win condition
                if self.revealed_count >= self.to_reveal:
                    self.print_board(reveal=True)
                    print("Congratulations — you revealed all safe cells! You win!")
                    break
            except ValueError:
                print("Invalid input. Please enter integer coordinates only.")
            except (KeyboardInterrupt, EOFError):
                print("\nExiting game.")
                break

if __name__ == "__main__":
    # Allow quick CLI customization if desired (optional)
    w, h, m = 10, 10, 10
    if len(sys.argv) == 4:
        try:
            w = int(sys.argv[1]); h = int(sys.argv[2]); m = int(sys.argv[3])
        except ValueError:
            print("Usage: python3 minesweeper_fixed.py [width height mines]")
            sys.exit(1)

    game = Minesweeper(width=w, height=h, mines=m)
    game.play()#!/usr/bin/env python3
import random
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = max(1, int(width))
        self.height = max(1, int(height))
        max_mines = self.width * self.height - 1
        mines = int(mines)
        # Cap mines to a sane value (at least one non-mine cell)
        if mines < 0:
            mines = 0
        if mines > max_mines:
            mines = max_mines
        self.mines = set(random.sample(range(self.width * self.height), mines))
        self.field = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.revealed = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.total_cells = self.width * self.height
        self.mines_count = len(self.mines)
        self.to_reveal = self.total_cells - self.mines_count
        self.revealed_count = 0

    def print_board(self, reveal=False):
        clear_screen()
        # Column header
        header = '   ' + ' '.join(f'{i:2}' for i in range(self.width))
        print(header)
        for y in range(self.height):
            row = f'{y:2} '
            for x in range(self.width):
                idx = y * self.width + x
                if reveal or self.revealed[y][x]:
                    if idx in self.mines:
                        row += ' *'
                    else:
                        count = self.count_mines_nearby(x, y)
                        row += f' {count}' if count > 0 else '  '
                else:
                    row += ' .'
            print(row)

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Validate coordinates
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # treat as no-op (play() will inform user about bounds)
        idx = y * self.width + x
        if idx in self.mines:
            # Hit a mine
            return False

        # Iterative flood-fill to reveal connected empty area (avoid recursion)
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if self.revealed[cy][cx]:
                continue
            # If it's a mine, skip revealing it (shouldn't happen because we checked initial)
            if (cy * self.width + cx) in self.mines:
                continue
            self.revealed[cy][cx] = True
            self.revealed_count += 1
            # If this cell has no adjacent mines, reveal neighbors
            if self.count_mines_nearby(cx, cy) == 0:
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            # Do not add neighbor if it's a mine
                            if (ny * self.width + nx) not in self.mines:
                                stack.append((nx, ny))
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                raw_x = input("Enter x coordinate: ").strip()
                raw_y = input("Enter y coordinate: ").strip()
                if raw_x == '' or raw_y == '':
                    print("Please enter both coordinates.")
                    continue
                x = int(raw_x)
                y = int(raw_y)
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordinates out of bounds. x must be 0..{self.width-1}, y must be 0..{self.height-1}.")
                    continue
                ok = self.reveal(x, y)
                if not ok:
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                # Check win condition
                if self.revealed_count >= self.to_reveal:
                    self.print_board(reveal=True)
                    print("Congratulations — you revealed all safe cells! You win!")
                    break
            except ValueError:
                print("Invalid input. Please enter integer coordinates only.")
            except (KeyboardInterrupt, EOFError):
                print("\nExiting game.")
                break

if __name__ == "__main__":
    # Allow quick CLI customization if desired (optional)
    w, h, m = 10, 10, 10
    if len(sys.argv) == 4:
        try:
            w = int(sys.argv[1]); h = int(sys.argv[2]); m = int(sys.argv[3])
        except ValueError:
            print("Usage: python3 minesweeper_fixed.py [width height mines]")
            sys.exit(1)

    game = Minesweeper(width=w, height=h, mines=m)
    game.play()
