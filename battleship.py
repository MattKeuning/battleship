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
        row = int(input("What row would you like the front/right of you ship to be on (1-10) "))
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
        time.sleep(2)
        print(f"Okay, {p1name} now that {p2name} is gone lets get to work!")
        while p1lengths:
            p1ship = player1.set_ship_coordinates()
            h_or_v = input("Would you like your ship to be horizontal or verticle (h/v) ")
            length = int(input("What length would you like this ship to have (keep in mind you will set 4 ships: lengths 2-5) "))
            for i in range(length):
                if h_or_v == 'v':
                    p1board.show_ships[p1ship[0]+i][p1ship[1]] = 'S'
                    p1board.ships.append((p1ship[0]+i,p1ship[1]))
                else:
                    p1board.show_ships[p1ship[0]][p1ship[1]-i] = 'S'
                    p1board.ships.append((p1ship[0],p1ship[1]-i))
            p1lengths.remove(length)
        print(f'Perfect! Here is what your board now looks like:')
        print(p1board.show_ships_on_board())
        time.sleep(3)
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
        while p2lengths:
            p2ship = player2.set_ship_coordinates()
            h_or_v = input("Would you like your ship to be horizontal or verticle (h/v) ")
            length = int(input("What length would you like this ship to have (keep in mind you will set 4 ships: lengths 2-5) "))
            for i in range(length):
                if h_or_v == 'v':
                    p2board.show_ships[p1ship[0]+i][p1ship[1]] = 'S'
                    p2board.ships.append((p2ship[0]+i,p2ship[1]))
                else:
                    p2board.show_ships[p1ship[0]][p1ship[1]-i] = 'S'
                    p2board.ships.append((p2ship[0],p1ship[1]-i))
            p2lengths.remove(length)
        print(f'Perfect! Here is what your board now looks like:')
        print(p2board.show_ships_on_board())
        time.sleep(3)
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
                row = input(f'{p1name} pick a row! ')
                col = input(f'Also a column! ')
                time.sleep(3)
                if p2board.shoot(row, col):
                    print("BOOM YOU\'VE GOT A HIT")
                else:
                    print("Sorry, you missed")
            else:
                print(f'Okay, {p2name} here is what you\'re working with...')
                time.sleep(2)
                p1board.print_board()
                row = input(f'{p2name} pick a row! ')
                col = input(f'Also a column! ')
                time.sleep(3)
                if p1board.shoot(row, col):
                    print("BOOM YOU\'VE GOT A HIT")
                else:
                    print("Sorry, you missed")
        if winner == p1name:
            print(f"Congratulations {p1name}, you have won the game!!!")
        else:
            print(f"Congratulations {p1name}, you have won the game!!!")
        return

        



if __name__ == "__main__":
    game = Game()
    board = Board()
    game.play()