import tkinter as tk
from tkinter import messagebox

def check_win(player, row, col):
    for c in range(COLS - 3):
        if all(board[row][c + i] == player for i in range(4)):
            return True
    for r in range(ROWS - 3):
        if all(board[r + i][col] == player for i in range(4)):
            return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(3, COLS):
            if all(board[r + i][c - i] == player for i in range(4)):
                return True
    return False

def drop_token(col):
    global current_player, winner, count
    if winner is not None:
        return
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = current_player + 1
            canvas.create_oval(col * TOKEN_SIZE, row * TOKEN_SIZE, (col + 1) * TOKEN_SIZE, (row + 1) * TOKEN_SIZE, fill=PLAYER_COLORS[current_player])
            count += 1
            if check_win(current_player + 1, row, col):
                winner = current_player + 1
                messagebox.showinfo("Connect 4", f'Player {winner} wins!')
            elif count == ROWS * COLS and winner is None:
                messagebox.showinfo("Connect 4", "It's a tie!")
            else:
                current_player = 1 - current_player
            return

def reset():
    global count, winner
    canvas.delete("all")
    count = 0
    winner = None
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

# Initialize the game settings and board
ROWS = 6
COLS = 7
TOKEN_SIZE = 60
PLAYER_COLORS = ['red', 'yellow']
board = [[0] * COLS for _ in range(ROWS)]
current_player = 0
winner = None
count = 0

root = tk.Tk()
root.title('Connect Four')
root.configure(bg='blue')
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP)
for col in range(COLS):
    tk.Button(button_frame, text=str(col + 1), command=lambda c=col: drop_token(c)).pack(side=tk.LEFT, padx=10)
canvas = tk.Canvas(root, width=COLS * TOKEN_SIZE, height=ROWS * TOKEN_SIZE, bg="blue")
canvas.create_rectangle(0, 0, COLS * TOKEN_SIZE, ROWS * TOKEN_SIZE, outline='blue')
canvas.pack()
menu = tk.Menu(root)
root.config(menu=menu)
options = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset Game", command=reset)
root.mainloop()