import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                               command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def on_click(self, row, col):
        btn = self.buttons[row][col]
        if btn['text'] == "" and not self.check_winner():
            btn['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = [self.buttons[i] for i in range(3)] # Rows
        lines += [[self.buttons[r][i] for r in range(3)] for i in range(3)] # Columns
        lines += [[self.buttons[i][i] for i in range(3)]] # Diagonal \
        lines += [[self.buttons[i][2-i] for i in range(3)]] # Diagonal /

        for line in lines:
            if line[0]['text'] == line[1]['text'] == line[2]['text'] != "":
                return True
        return False

    def check_draw(self):
        return all(self.buttons[row][col]['text'] != "" for row in range(3) for col in range(3))

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
