

def is_numbric(number: str):
    while not number.isdigit():
        number = input("insert a number")
    return int(number)


def position_check(position: str, num):
    while True:
        if not position.count(" ") == 1:
            position = input("please insert position with one space between the numbers: ")
            continue
        if not position[1].isspace():
            position = input("please insert position with space: ")
            continue
        if not position.split()[1].isdigit():
            position = input("please insert position with numbers: ")
            continue
        if not position.split()[0].isdigit():
            position = input("please insert position with numbers: ")
            continue
        if not len(position.split()) < 3:
            position = input("please insert position: ")
            continue
        if  int(position.split()[0]) > num or int(position.split()[1]) > num:
            position = input(f"please insert position between range {num}  : ")
            continue
        if int(position.split()[0]) <= 0 or int(position.split()[1]) <= 0 :
            position = input(f"please insert position between range 1-{num}: ")
            continue

        return position


class TicTacToe:
    l = ["X", "O"]

    def __init__(self, number_list, game_table):

        self.number_list = number_list
        self.game_table = game_table

    def add_assign(self, position, player, player_name):
        column, line = position.split()
        self.is_empty(column, line)
        self.game_table[int(column) - 1][int(line) - 1] = self.l[player]
        x = self.check_win(player_name)
        self.print_game()
        if x:
            return True

    def is_empty(self, column, line):
        while True:
            if self.game_table[int(column) - 1][int(line) - 1] != " ":
                colum, line = input("please insert position again. the position not empty:")

            else:
                return None

    def check_win(self, player_name):
        # horizontal win
        for i in self.game_table:
            for j in i:
                if j == " ":
                    break
                if i[1:] == i[:-1]:
                    print(f"Congratulations {player_name} won the game ")
                    return True

            break
        # vertical win
        for i, e in enumerate(self.game_table):
            count = 0
            curr_chat = e[i]
            for j in self.game_table:
                if j[i] == " ":
                    break
                if j[i] == curr_chat:
                    count += 1
                else:
                    break
            if count == len((self.game_table)):
                print(f"Congratulations {player_name} won the game  ")
                return True

        # left diagonal win
        curr_chat = self.game_table[0][0]
        count = 0
        for i in range(len(self.game_table)):
            if self.game_table[i][i] == " ":
                break
            if self.game_table[i][i] == curr_chat:
                count += 1
            else:
                break
        if count == len(self.game_table):
            print(f"Congratulations {player_name} won the game")
            return True
        #  right diagonal win
        curr_chat = self.game_table[0][-1]
        count = 0
        for i in range(len(self.game_table)):
            if self.game_table[i][size - 1 - i] == " ":
                break
            if self.game_table[i][size - 1 - i] == curr_chat:
                count += 1
            else:
                break
        if count == len(self.game_table):
            print(f"Congratulations {player_name} won the game")
            return True



    def print_game(self):
        print("-", end="     |   ")
        for i in self.number_list:
            print(i, end="   |     ")
        print()
        for i, n in enumerate(self.game_table):
            print("-----------" * len(self.game_table))
            print(i + 1, end="    |    ")

            for j in range(len(self.game_table)):
                print(n[j], end='   |     ')
            print()
        print("\n")



print(
    '''
 __          __  _                                _             _   ___     ___      
 \ \        / / | |                              | |           | \ | \ \   / ( )     
  \ \  /\  / /__| | ___ ___  _ __ ___   ___      | |_ ___      |  \| |\ \_/ /|/ ___  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \     | __/ _ \     | . ` | \   /   / __| 
    \  /\  /  __/ | (_| (_) | | | | | |  __/     | || (_) |    | |\  |  | |    \__ \ 
  ___\/__\/ \___|_|\___\___/|_|_|_| |_|\___|      \__\___/____ |_| \_|  |_|    |___/ 
 |__   __(_)               |__   __|                  |__   __|                      
    | |   _  ___   ______     | | __ _  ___   ______     | | ___   ___               
    | |  | |/ __| |______|    | |/ _` |/ __| |______|    | |/ _ \ / _ \              
    | |  | | (__              | | (_| | (__              | | (_) |  __/              
    |_|  |_|\___|             |_|\__,_|\___|             |_|\___/ \___|     
    '''
)





first_player_name = input("player 1 name (X): ")
second_player_name = input("player 2 name (O): ")

size =is_numbric(input("insert the game table size: "))
while size < 3 or size > 9:
    size = is_numbric(input("please insert size between 3 and 9: "))


player1, player2 = 0, 1


number_list = []
tic_tac_toe_list = []
for i in range(int(size)):
    number_list.append(i + 1)
    tic_tac_toe_list.append([])
for j in tic_tac_toe_list:
    for i in range(int(size)):
        j.append(" ")
t = TicTacToe(number_list, tic_tac_toe_list)
t.print_game()
while True:
    position = position_check(input("pleas enter position: "),size)
    x = t.add_assign(position,player1,first_player_name)
    if x:
        break
    position = position_check(input("pleas enter position: "),size)
    x = t.add_assign(position, player2, second_player_name)
    if x:
        break


