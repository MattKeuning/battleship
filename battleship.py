from typing import List

class Player:

    def __init__(self, player_name: str):
        self.player_name = player_name

    def get_name(self):
        return self.player_name
    
    def set_name(self, name):
        self.player_name = name

    def set_ship_coordinates(self):
        # Asking for rows and columns in 1 indexed notation to make it more intuitive
        row = input("What row would you like the front/right of you ship to be on (1-10)")
        row -= 1
        col = input("What column would you like the front/right of your ship to be on (1-10)")
        col -= 1
        return (row, col)

class Board:

    def __init__(self):
        self.board = self.generate_new_board()
        self.ships = list()

    def generate_new_board(self):
        return [
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
            ["~"]*10,
        ]
    
    def print_board(self):
        for i in range(len(self.board)):
            if i != 0:
                print('\n')
            for j in self.board[i]:
                print(j, end='\t')
        return '\n'
    
    def shoot(self, row: int, col: int):
        if (row, col) in self.ships:
            self.board[row][col] = 'H'
            return True
        else:
            self.board[row][col] = 'O'
            return False

class Game:

    def __init__(self):
        self.game_over = False
        self.player1 = None
        self.player2 = None

    def play(self):
        while not self.game_over:
            pass



if __name__ == "__main__":
    game = Game()
    board = Board()
    print(board.print_board())