import random
import numpy as np

class Player():
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol


class Game():
    def __init__(self):
        self.board = [["-"]*3,["-"]*3,["-"]*3]
        self.show_board()

    def show_board(self):
        print()
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print()
        print('eg')

    def setup_game(self):
        print('WELCOME TO TIC TAC TOE!')

        human_name = input('Human name? >> ') 

        while True:
            try:
                human_sign = str(input('Human sign: X or O >> '))
                if human_sign in ['X','O']:
                    if human_sign == 'X':
                        pc_sign = 'O'
                    else:
                        pc_sign = 'X'

                    print(f'Computer will be {pc_sign}')
                    break
                else:
                    raise Exception
            except:
                print('Please choose one of the signs: X or O')

        human = Player(human_name,human_sign)
        pc = Player('pc',pc_sign)

        first_player_random = random.choice([0,1])

        if first_player_random == 0:
            first_player = human
        else:
            first_player = pc

        print(f'Ready! The first player to start is {first_player.name}')
        return human, pc, first_player_random


    def turn(self,player):
        possible_spaces = self.check_spaces("-")   
        if len(possible_spaces) == 0:
            print(F'GAME OVER! WE HAVE A TIE')
            return True

        if player.name=='pc':
            position = random.choice(possible_spaces)
            print(f"It is {player.name}'s turn! Position chosen was {position} ")
        else:
            while True:
                try:
                    position = input(f"It is {player.name}'s turn! Please choose a square from 1 to 9: ")
                    if int(position) in possible_spaces:
                        break
                    else:
                        raise Exception

                except ValueError as ve:
                    print('The input value must be a number!')
                except:
                    print('Please choose a possible square!')
    
        self.fill_space(position,player.symbol)
        self.show_board()

        return self.check_winner(player.symbol)

    def fill_space(self,space_index,symbol):
        space_index = int(space_index)
        row = np.ceil(space_index/3)-1
        col = space_index - 1 - 3*row

        self.board[int(row)][int(col)] = symbol

    def check_spaces(self,symbol):
        spaces_true = []

        for i in range(len(self.board)):
            for j,val in enumerate(self.board[i]):
                if val == symbol:
                    space_index = j+3*i+1
                    spaces_true.append(space_index)
        
        return spaces_true

    def check_horizontal(self,symbol):
        nr_rows = len(self.board)
        for i in range(0,nr_rows):
            count = self.board[i].count(symbol)
            print(f'count horizontal {count}')
            print(self.board[i])
            if count == 3:
                return True
        return False

    def check_vertical(self,symbol):
        nr_rows = len(self.board)
        for i in range(0,nr_rows):
            count = 0
            for j in range(0,len(self.board[i])):
                if self.board[i][j]==symbol:
                    count += 1
            print(f'count vertical {count}')
            if count == 3:
                return True

        return False

    def check_diagonal(self,symbol):
        nr_rows = len(self.board)

        for i in range(0,nr_rows):
            count_left = 0
            count_right = 0

            if self.board[i][i]==symbol:
                count_left += 1
            if self.board[i][len(self.board[i])-1-i]==symbol:
                count_right+=1
            
            print(f'count left diag {count_left}')
            print(f'count right diag {count_right}')

            if count_left == 3 or count_right == 3:
                return True  
            else:
                return False


    def check_winner(self,symbol):
        # check horizontal
        if self.check_horizontal(symbol):
            return True
        elif self.check_vertical(symbol):
            return True
        elif self.check_diagonal(symbol):
            return True
        else:
            return False

if __name__ == '__main__':
    new_game = Game()
    human, pc, first_player_index = new_game.setup_game()

    winner_found = False
    while not winner_found:
        if first_player_index == 0:
            winner_found = new_game.turn(human)
            winner_found = new_game.turn(pc)
        else:
            winner_found = new_game.turn(pc)
            winner_found = new_game.turn(human)

        
        