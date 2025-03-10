class Player:

    def __init__(self, player_name: str):
        self.player_name = player_name

    def get_name(self):
        return self.player_name
    
    def set_name(self, name):
        self.player_name = name


class Board:

    def __init__(self):
        self.board = self.generate_new_board()

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

class Game:

    pass



if __name__ == "__main__":
    game = Game()
    board = Board()
    print(board.print_board())