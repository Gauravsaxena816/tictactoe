import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import TicTacToe, minimax

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = TicTacToe()
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.root, text=" ", font='normal 36 bold', height=4, width=8, command=lambda row=row, col=col: self.click_button(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def click_button(self, row, col):
        square = row * 3 + col
        if self.board.board[square] == ' ':
            self.board.make_move(square, 'X')
            self.update_buttons()
            if self.board.current_winner:
                self.end_game("Player X wins!")
                return
            elif not self.board.empty_squares():
                self.end_game("It's a tie!")
                return

            self.make_ai_move()
            self.update_buttons()
            if self.board.current_winner:
                self.end_game("Player O wins!")
            elif not self.board.empty_squares():
                self.end_game("It's a tie!")

    def make_ai_move(self):
        best_move = minimax(self.board, 'O')['position']
        self.board.make_move(best_move, 'O')

    def update_buttons(self):
        for row in range(3):
            for col in range(3):
                square = row * 3 + col
                self.buttons[row][col]['text'] = self.board.board[square]

    def end_game(self, result):
        messagebox.showinfo("Game Over", result)
        self.reset_game()

    def reset_game(self):
        self.board = TicTacToe()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ' '

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
