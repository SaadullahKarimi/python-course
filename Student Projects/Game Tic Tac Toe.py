# Import the tkinter library for GUI components and messagebox for alerts  
import tkinter as tk  
from tkinter import messagebox  

# Define the TicTacToe class to encapsulate the game logic and UI  
class TicTacToe:  
    # Initialize the game with the main window (root)  
    def __init__(self, root):  
        self.root = root  # Store the main window reference  
        self.root.title("TIC TAC TOE GAME")  # Set the window title  
        self.root.configure(bg='lightblue')  # Set the background color of the main window  

        # Initialize variables for the game state  
        self.current_player = "X"  # Set the first player to X  
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # Create a 3x3 board initialized with spaces  
        self.player_x_score = 0  # Initialize Player X's score  
        self.player_o_score = 0  # Initialize Player O's score  

        # Create a 3x3 grid to hold button references for the game board  
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  
        self.create_widgets()  # Call method to create the GUI elements  
        self.update_scoreboard()  # Update the scoreboard display  

    # Method to create the buttons and scoreboard in the UI  
    def create_widgets(self):  
        # Create the buttons for the Tic Tac Toe board  
        for i in range(3):  
            for j in range(3):  
                # Create a button for each cell in the 3x3 grid  
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=('Arial', 40), width=5, height=2,  
                                                bg='blue', activebackground='lightgreen',  # Set button background colors  
                                                command=lambda row=i, col=j: self.make_move(row, col))  
                self.buttons[i][j].grid(row=i, column=j)  # Place the button in the grid  

        # Create a label to display the scores for both players  
        self.score_label = tk.Label(self.root, text=f"Player X: {self.player_x_score}   Player O: {self.player_o_score}", font=('Arial', 20), bg='lightblue')  
        self.score_label.grid(row=3, columnspan=3)  # Position the score label below the buttons  

        # Create an exit button to close the application  
        self.exit_button = tk.Button(self.root, text="EXIT", command=self.root.quit, fg='red', bg='lightcoral')  
        self.exit_button.grid(row=4, column=2)  # Place the exit button on the grid  

    # Method to handle a player's move  
    def make_move(self, row, col):  
        # Check if the selected cell is empty  
        if self.board[row][col] == " ":  
            # Update the board with the current player's mark  
            self.board[row][col] = self.current_player  
            self.buttons[row][col].config(text=self.current_player)  # Update the button text  

            # Check if the current player has won  
            if self.check_winner():  
                self.show_winner(self.current_player)  # Show the winner message  
                # Update the score based on the current player  
                if self.current_player == "X":  
                    self.player_x_score += 1  
                else:  
                    self.player_o_score += 1  
                self.update_scoreboard()  # Refresh the scoreboard display  
                self.root.after(2000, self.reset_game)  # Automatically reset the game after 2 seconds  

            # Check if the board is full, indicating a tie  
            elif self.is_full():  
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")  # Show tie message  
                self.update_scoreboard()  # Refresh the scoreboard display  
                self.root.after(2000, self.reset_game)  # Automatically reset the game after 2 seconds  

            # Switch to the other player  
            else:  
                self.current_player = "O" if self.current_player == "X" else "X"  

    # Method to check if there is a winner  
    def check_winner(self):  
        # Check all rows for a winning condition  
        for i in range(3):  
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":  
                return True  # Return True if a row has the same non-empty value  

        # Check all columns for a winning condition  
        for i in range(3):  
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":  
                return True  # Return True if a column has the same non-empty value  

        # Check the two diagonals for a winning condition  
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":  
            return True  # Return True if the main diagonal has the same non-empty value  
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":  
            return True  # Return True if the anti-diagonal has the same non-empty value  

        return False  # Return False if no winner is found  

    # Method to check if the board is full (indicating a tie)  
    def is_full(self):  
        # Return True if all cells are filled  
        return all(all(cell != " " for cell in row) for row in self.board)  

    # Method to display a message box announcing the winner  
    def show_winner(self, player):  
        messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")  # Show winner message  

    # Method to update the scoreboard display  
    def update_scoreboard(self):  
        self.score_label.config(text=f"Player X: {self.player_x_score}   Player O: {self.player_o_score}")  # Update score label  

    # Method to reset the game state for a new game  
    def reset_game(self):  
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # Reset the board to empty  
        self.current_player = "X"  # Reset the current player to X  
        # Clear the text of all buttons on the board  
        for row in self.buttons:  
            for button in row:  
                button.config(text=" ")  

# Main execution block to run the game  
if __name__ == "__main__":  
    root = tk.Tk()  # Create the main window  
    game = TicTacToe(root)  # Instantiate the TicTacToe class  
    root.mainloop()  # Start the