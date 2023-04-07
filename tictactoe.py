import tkinter as tk
import numpy as np
import tensorflow as tf
from neuralnetwork import neural_network

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Create the game board
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        # Define the players and starting player
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1

        # Create the buttons
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    master, text="", font=("Helvetica", 20), width=4, height=2,
                    command=lambda row=row, col=col: self.make_move(row, col)
                )
                button.grid(row=row, column=col, sticky="nsew")
                button_row.append(button)
            self.buttons.append(button_row)



    def make_move(self, row, col):
        if self.board[row][col] == "":
            # Update the board with the player's move
            self.board[row][col] = self.current_player

            # Update the button text and color
            self.buttons[row][col].config(text=self.current_player, bg="light gray")

            # Check for a win or draw
            winner = self.check_win()
            if winner is not None:
                self.game_over(winner)
            elif self.current_player == self.player2:
                board_state = self.get_board_state()
                computer_move = neural_network(board_state)
                self.make_move(computer_move[0], computer_move[1])
            else:
                self.current_player = self.player1

    def get_board_state(self):
        # Convert the board state to a 3x3 numpy array
        board_state = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.player1:
                    board_state[i][j] = 1
                elif self.board[i][j] == self.player2:
                    board_state[i][j] = -1
        return board_state

    def get_computer_move(self, board_state):
        # Use the neural network to get the computer's move
        # The neural network should take a 3x3 numpy array as input
        # and output a tuple of row and column numbers
        computer_move = neural_network(board_state)
        return computer_move

    def check_win(self):
        # Check for horizontal wins
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return row[0]

        # Check for vertical wins
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return self.board[0][col]

        # Check for diagonal wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        # Check for draw
        if all(row.count("") == 0 for row in self.board):
            return "draw"

        # No winner or draw
        return None

    def game_over(self, winner):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")
        if winner == "draw":
            message = "The game is a draw!"
        else:
            message = f"Player {winner} wins!"
        label = tk.Label(self.master, text=message, font=("Helvetica", 20))
        label.grid(row=3, column=0, columnspan=3)

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
