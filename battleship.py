from typing import List
import time

class Player:

    def __init__(self, player_name: str):
        self.player_name = player_name

    def get_name(self):
        return self.player_name
    
    def set_name(self, name):
        self.player_name = name

    def set_ship_coordinates(self):
        # Asking for rows and columns in 1 indexed notation to make it more intuitive
        row = int(input("\n\nWhat row would you like the front/right of you ship to be on (1-10) "))
        row -= 1
        col = int(input("What column would you like the front/right of your ship to be on (1-10) "))
        col -= 1
        return (row, col)

class Board:

    def __init__(self):
        self.board = self.generate_new_board()
        self.show_ships = self.generate_new_board()
        self.ships = list()
        self.count = 0
        self.visual = [
            [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10)],
            [(2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9), (2,10)],
            [(3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9), (3,10)],
            [(4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9), (4,10)],
            [(5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,10)],
            [(6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9), (6,10)],
            [(7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9), (7,10)],
            [(8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10)],
            [(9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9), (9,10)],
            [(10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9), (10,10)],
            
        ]

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
    
    def help_player_visualize(self):
        for i in range(len(self.visual)):
            if i != 0:
                print('\n')
            for j in self.visual[i]:
                if i != len(self.visual)-1:
                    print(j, end='\t ')
                else:
                    print(j, end='\t')
        return '\n'
    
    def show_ships_on_board(self):
        for i in range(len(self.show_ships)):
            if i != 0:
                print('\n')
            for j in self.show_ships[i]:
                print(j, end='\t')
        return '\n'
    
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
            self.count += 1
            return True
        else:
            self.board[row][col] = 'O'
            return False
        
    def clear(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        return '\n'

class Game:

    def __init__(self):
        self.game_over = False
        self.player1 = None
        self.player2 = None

    def play(self):
        winner = None
        p1lengths = [2,3,4,5]
        p2lengths = [2,3,4,5]
        print("Welcome to BattleShip!")
        p1name = input("Player one, what is your name? ")
        p2name = input("Player two, what is your name? ")
        player1 = Player(p1name)
        player2 = Player(p2name)
        p1board = Board()
        p2board = Board()
        time.sleep(1)
        print(f"{p2name} please give me and {p1name} some privacy while we set up {p1name}\'s ships!")
        time.sleep(4)
        print(f"Okay, {p1name} now that {p2name} is gone lets get to work!")
        print(f'\n\nBefore we begin here is a reference for what the coordinates will look like (row, column):\n')
        while p1lengths:
            p1board.help_player_visualize()
            p1ship = player1.set_ship_coordinates()
            h_or_v = input("Would you like your ship to be horizontal or verticle (h/v) ")
            length = int(input("What length would you like this ship to have (keep in mind you will set 4 ships: lengths 2-5) "))
            for i in range(length):
                if h_or_v == 'v':
                    p1board.show_ships[p1ship[0]+i][p1ship[1]] = 'S'
                    p1board.ships.append((p1ship[0]+i,p1ship[1]))
                    p1board.visual[p1ship[0]+i][p1ship[1]] = 'HHHHH'
                else:
                    p1board.show_ships[p1ship[0]][p1ship[1]-i] = 'S'
                    p1board.ships.append((p1ship[0],p1ship[1]-i))
                    p1board.visual[p1ship[0]][p1ship[1]-i] = 'HHHHH'
            p1lengths.remove(length)
        print(f'Perfect! Here is what your board now looks like:')
        print(p1board.show_ships_on_board())
        time.sleep(5)
        print(f'Now this will erase in 3!')
        time.sleep(1)
        print(f'2!')
        time.sleep(1)
        print(f'1!')
        time.sleep(1)
        p1board.clear()
        print(f"Now please be a dear and pass the screen to {p2name}")
        time.sleep(3)
        print(f'Welcome back, {p2name}!\nLets set up your ships now!')
        print(f'\n\nBefore we begin here is a reference for what the coordinates will look like (row, column):\n')
        while p2lengths:
            p2board.help_player_visualize()
            p2ship = player2.set_ship_coordinates()
            h_or_v = input("Would you like your ship to be horizontal or verticle (h/v) ")
            length = int(input("What length would you like this ship to have (keep in mind you will set 4 ships: lengths 2-5) "))
            for i in range(length):
                if h_or_v == 'v':
                    p2board.show_ships[p2ship[0]+i][p2ship[1]] = 'S'
                    p2board.ships.append((p2ship[0]+i,p2ship[1]))
                    p2board.visual[p2ship[0]+i][p2ship[1]] = 'HHHHH'
                else:
                    p2board.show_ships[p2ship[0]][p2ship[1]-i] = 'S'
                    p2board.ships.append((p2ship[0],p2ship[1]-i))
                    p2board.visual[p2ship[0]][p2ship[1]-i] = 'HHHHH'
            p2lengths.remove(length)
        print(f'Perfect! Here is what your board now looks like:')
        print(p2board.show_ships_on_board())
        time.sleep(5)
        print(f'Now this will erase in 3!')
        time.sleep(1)
        print(f'2!')
        time.sleep(1)
        print(f'1!')
        time.sleep(1)
        p2board.clear()
        p1turn = True
        while not self.game_over:
            if p1board.count == 14:
                winner = p1name
                break
            elif p2board.count == 14:
                winner = p2name
                break
            if p1turn:
                print(f'Okay, {p1name} here is what you\'re working with...')
                time.sleep(2)
                p2board.print_board()
                row = int(input(f'{p1name} pick a row! ')) - 1
                col = int(input(f'Also a column! ')) - 1
                time.sleep(1)
                if p2board.shoot(row, col):
                    print("BOOM YOU\'VE GOT A HIT")
                else:
                    print("Sorry, you missed")
            else:
                print(f'Okay, {p2name} here is what you\'re working with...')
                time.sleep(2)
                p1board.print_board()
                row = int(input(f'{p2name} pick a row! ')) - 1
                col = int(input(f'Also a column! ')) - 1
                time.sleep(1)
                if p1board.shoot(row, col):
                    print("BOOM YOU\'VE GOT A HIT")
                else:
                    print("Sorry, you missed")
            if p1turn:
                p1turn = False
            else:
                p1turn = True
        if winner == p1name:
            print(f"Congratulations {p1name}, you have won the game!!!")
        else:
            print(f"Congratulations {p1name}, you have won the game!!!")
        return

        



if __name__ == "__main__":
    game = Game()
    board = Board()
    game.play()