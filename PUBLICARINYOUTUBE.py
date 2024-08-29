

"""
This program is an implementation of the classic
board game "Connect Four" in Python. The objective
of the game is for two players to take turns dropping
pieces into a vertical grid, with the aim of being
the first to form a horizontal, vertical, or diagonal line
of four of their own pieces
"""
#https://github.com/MarlenFineza/Marlen-Diaz-Castelo/blob/main/PUBLICARINYOUTUBE.py

# Number of columns and rows for the Connect Four board
numcol = 7
numrow = 6

# Class to encapsulate the Connect Four game logic
class conectaFour():
    
    # Constructor method to initialize the game
    def __init__(self):
        # Start with player 'A'
        self.player = 'A'
        # Create a 2D list (6x7) filled with empty spaces to represent the board
        self.board = [[' ' for _ in range(numcol)] for _ in range(numrow)]
    
    # Method to print the current state of the board
    def printBoard(self):
        for row in self.board:
            # Join the row elements with ' | ' and print it
            print(' | '.join(row))
            # Print a line to separate rows
            print('-------------------------')
    
    # Method to drop a piece in the specified column
    def Drowpiece(self, col):
        # Start checking from the bottom row upwards
        for row in range(5, -1, -1):
            # If the current cell is empty, place the player's piece here
            if self.board[row][col] == ' ':
                self.board[row][col] = self.player
                return True  # Indicate that the piece was successfully placed
        return False  # If the column is full, return False
    
    # Method to switch the current player
    def switchPlayer(self):
        if self.player == 'A':
            self.player = 'B'  # Switch to player 'B'
        else:
            self.player = 'A'  # Switch back to player 'A'
    
    # Method to check for winning conditions
    def winsCondition(self):
        # Check horizontal win conditions
        for row in range(numrow):
            for col in range(numcol - 3):
                # Check four consecutive cells horizontally
                if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] != ' ':
                    return True
        
        # Check vertical win conditions
        for col in range(numcol):
            for row in range(numrow - 3):
                # Check four consecutive cells vertically
                if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] != ' ':
                    return True
        
        # Check diagonal win conditions (top left to bottom right)
        for row in range(numrow - 3):
            for col in range(numcol - 3):
                # Check four consecutive cells diagonally from top left to bottom right
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != ' ':
                    return True
        
        # Check diagonal win conditions (top right to bottom left)
        for row in range(3, numrow):
            for col in range(numcol - 3):
                # Check four consecutive cells diagonally from top right to bottom left
                if self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3] != ' ':
                    return True
        
        return False  # Return False if no winning condition is met

    """
    This program is an implementation of the classic board
    game "Connect Four" in Python. The objective of the game
    is for two players to take turns dropping pieces into
    a vertical grid, with the aim of being the first to
    form a horizontal, vertical, or diagonal
    line of four of their own pieces
    """


    # Method to manage the game loop and determine the winner
    def Wins(self):
        while True:
            self.printBoard()  # Display the current board state
            # Prompt the current player to choose a column
            col = int(input(f"Player {self.player}, enter a column between (0-6):"))
            # Drop the piece in the selected column
            self.Drowpiece(col)
            # Check if the current player has won
            if self.winsCondition():
                self.printBoard()  # Display the final board state
                print(self.player, "wins")  # Announce the winner
                break  # Exit the game loop
            # Check if the board is full and the game is a tie
            if all(self.board[i][j] != ' ' for i in range(numrow) for j in range(numcol)):
                self.printBoard()  # Display the final board state
                print("Game tied")  # Announce that the game is tied
                break  # Exit the game loop
            self.switchPlayer()  # Switch to the next player for the next turn
        return False  # End the game
    
# Create an instance of the game and start it
ok = conectaFour()
ok.Wins()
