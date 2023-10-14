import tkinter as tk

with open('/Users/bilgehanors/Desktop/2_Game_of_Life/book.txt', 'r') as file:
    lines = file.readlines()[1:]
GRID_SIZE = (len(lines)+1)
CELL_SIZE = 20
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for row, line in enumerate(file):
                if row < GRID_SIZE:
                    values = line.split()
                    for col in range(min(len(values), GRID_SIZE)):
                        grid[row][col] = int(values[col])
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    create_grid()

root = tk.Tk()
root.title("Game of Life")

canvas = tk.Canvas(root)
canvas.pack()

next_gen_button = tk.Button(root, text="Next Generation")
next_gen_button.pack()

def next_generation():
    global grid
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            neighbors = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if 0 <= row + i < GRID_SIZE and 0 <= col + j < GRID_SIZE and grid[row + i][col + j] == 1:
                        neighbors += 1

            if grid[row][col] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[row][col] = 0
            elif grid[row][col] == 0 and neighbors == 3:
                new_grid[row][col] = 1
            else:
                new_grid[row][col] = grid[row][col]

    grid = new_grid
    create_grid()

next_gen_button.config(command=next_generation)

def create_grid():
    canvas.delete("all")
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x1, y1 = col * CELL_SIZE, row * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            if grid[row][col]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

read_file("/Users/bilgehanors/Desktop/2_Game_of_Life/book.txt")

root.mainloop()

