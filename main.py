import random
import numpy as np

class Player():
    def __init__(self,id,name,symbol):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.start = False

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

        human = Player(1,human_name,human_sign)
        pc = Player(2,'pc',pc_sign)
        players_list = [human,pc]
        random.shuffle(players_list)
        
        print(f'Ready! The first player to start is {players_list[0].name}')

        return players_list


    def turn(self,player):
        possible_spaces = self.check_spaces("-")   

        if len(possible_spaces) == 0:
            print(F'***** GAME OVER! WE HAVE A TIE *****')
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
            # print(f'count horizontal {count}')
            if count == 3:
                return True
        return False

    def check_vertical(self,symbol):
        nr_cols = len(self.board[0])
        for j in range(0,nr_cols):
            count = 0
            for i in range(0,len(self.board[j])):
                if self.board[i][j]==symbol:
                    count += 1
            # print(f'count vertical {count}')
            if count == 3:
                return True

        return False

    def check_diagonal(self,symbol):
        nr_rows = len(self.board)
        count_left = 0
        count_right = 0
        for i in range(0,nr_rows):
            if self.board[i][i]==symbol:
                count_left += 1
            if self.board[i][len(self.board[i])-1-i]==symbol:
                count_right += 1
            
            # print(f'count left diag {count_left}')
            # print(f'count right diag {count_right}')

        if count_left == 3 or count_right == 3:
            return True  
        else:
            return False


    def check_winner(self,symbol):
        # check horizontal
        # print(f'Checking winner for {symbol}')
        if self.check_horizontal(symbol):
            winner_found = True
        elif self.check_vertical(symbol):
            winner_found = True
        elif self.check_diagonal(symbol):
            winner_found = True
        else:
            winner_found = False

        if winner_found:
            print(F'***** Player {pl.name} WON! GAME END. *****')

        return winner_found

if __name__ == '__main__':
    new_game = Game()
    players_list = new_game.setup_game()

    winner_found = False
    while not winner_found:
        for pl in players_list:
            winner_found = new_game.turn(pl)     
