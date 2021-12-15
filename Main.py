
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    # Firstly, we need to define some lists.
    # These list include P1's and P2's boards, and an empty board.
    # During the game, players' board lists will be updated all the time. On the other hand, empty board will be always constant and unchanged.
    # In order to achieve that I used list comprehensison to create a new list every time an empty board is needed.


    ships = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
    board_P1 = [['-' for i in range(board_size)] for i in range(board_size)]
    board_P2 = [['-' for i in range(board_size)] for i in range(board_size)]
    board_blank = [['-' for i in range(board_size)] for i in range(board_size)]
    board_ = [[['-' for i in range(board_size)] for i in range(board_size)],[['-' for i in range(board_size)] for i in range(board_size)]]

    #Let's place the first players ships


    # The main mechanism of the game is the while-loop structure. While-loop helps to ask the user for a valid input if the given input is not valid.
    # I used two while loops in this homework: one for ship placement and one for attack phase.

    current_players_ship = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
    current_players_board = board_P1
    n = 1
    # While loop for the ship placement phase(for both players)
    while len(current_players_ship) > 0:

        #Let's first print the necessary info: how many hips will be placed, whose turn it is, etc.
        print_3d_list(board_)
        print_ships_to_be_placed()
        for ship in current_players_ship:
            print_single_element(ship.capitalize())
        print_empty_line()

        print_player_turn_to_place(n)
        print_to_place_ships()
        ship_info_input = input().strip().lower()
        ship_info = ship_info_input.split()

        #Now we can start to check for errors

        #We'll start with checking if the input is in correct format

        #If 4 elements are given
        if len(ship_info) != 4:
            print_incorrect_input_format()
            continue

        (ship_name, x, y, orient) = ship_info
        #If it's an integer
        try:
            x = int(x)
            y = int(y)
        except:
            print_incorrect_input_format()
            continue

        # Now let's if the given coordinates are in correct range
        if not (0 < x <= 10 and 0 < y <= 10):
            print_incorrect_coordinates()
            continue

        # Check if the given ship name is a valid name
        if ship_name not in ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']:
            print_incorrect_ship_name()
            continue

        # Check if the orientation is in correct format
        if orient not in ["v","h"]:
            print_incorrect_orientation()
            continue

        # Check whether if the ship is already placed
        if (ship_name not in current_players_ship) and (ship_name in ships):
            print_ship_is_already_placed(ship_name.capitalize())
            continue

        # Let's check if the ship is placed outside the board, what's meant here is whether if one or more tiles exceed the board limits.
        ship_len = ships[ship_name]
        if (orient == "h" and x + ship_len > 11) or (orient == "v" and y + ship_len > 11):
            print_ship_cannot_be_placed_outside(ship_name.capitalize())
            continue

        #Let's check if the ship is placed on an already occupied place
        collides = False
        if orient == "h":
            for i in range(ship_len):
                if current_players_board[y - 1][x + i - 1] == '#':
                    print_ship_cannot_be_placed_occupied(ship_name.capitalize())
                    collides = True
                    break
        if orient == "v":
            for j in range(ship_len):
                if current_players_board[y + j - 1][x - 1] == '#':
                    print_ship_cannot_be_placed_occupied(ship_name.capitalize())
                    collides = True
                    break
        if collides:
            continue

        #Now, inputs have just been checked, now we can be sure that they're valid, HOORAYY!!!
        #Let's continue to place ships then, shall we?

        #We remove the placed ship
        current_players_ship.pop(ship_name)

        #Let's place the ship on the board
        if orient == "h":
            for i in range(ship_len):
                current_players_board[y-1][x+i-1] = '#'
        if orient == "v":
            for j in range(ship_len):
                current_players_board[y+j-1][x-1] = '#'

        #Now, Let's update the board
        if current_players_board == board_P1:
            board_ = [board_P1, board_blank]
        if current_players_board == board_P2:
            board_ = [board_blank, board_P2]
        #Board will be printed in the beginning of the loop


        #Let's confirm!!!

        if len(current_players_ship) == 0:
            confirmed_bool = True

            print_3d_list(board_)

            while True:
                # print_3d_list(board_)
                print_confirm_placement()
                confirm_input = input().strip().lower()
                if confirm_input not in ['y','n']:
                    continue

                if confirm_input == 'n':
                    confirmed_bool = False
                    break
                if confirm_input == 'y':
                    confirmed_bool = True
                    break

            if confirmed_bool:
                if n == 1:  #If placement is confirmed and its P1's turn
                    n=2
                    board_ = [board_blank,board_P2]
                    current_players_ship = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
                    current_players_board = board_P2
                    continue
                if n == 2:  #If placement is confirmed and its P2's turn
                    n=1
                    board_ = [board_P1, board_blank]
                    break
            else:
                if n == 1:  #If placement is not confirmed and its P1's turn
                    board_P1 = [['-' for i in range(board_size)] for i in range(board_size)]
                    board_ = [board_P1, board_blank]
                    current_players_ship = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
                    current_players_board = board_P1
                    continue
                if n == 2:  #If placement is not confirmed and its P2's turn
                    board_P2 = [['-' for i in range(board_size)] for i in range(board_size)]
                    board_ = [board_blank, board_P2]
                    current_players_ship = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
                    current_players_board = board_P2
                    continue

    #Ship placement is over!!! BOOM-BA-YAA!!!
#########################################################################################################################3

    board_P1_in_enemy_vision = [['-' for i in range(board_size)] for i in range(board_size)]
    board_P2_in_enemy_vision = [['-' for i in range(board_size)] for i in range(board_size)]

    #Now we'll code the attack phase
    while True:

        #This lines of code determines if the game will end or continue
        set_of_characters = set()
        continue_to_game = True
        for line_1 in board_P1:
            for el in line_1:
                set_of_characters.add(el)
        if '#' not in set_of_characters:
            continue_to_game = False

        set_of_characters = set()
        for line_2 in board_P2:
            for el in line_2:
                set_of_characters.add(el)
        if '#' not in set_of_characters:
            continue_to_game = False

        if continue_to_game == False:
            print_3d_list([board_P1, board_P2])
            print_player_won(n)
            print_thanks_for_playing()
            break




        if n == 1:
            enemy_board = board_P2
            board_ = [board_P1,board_P2_in_enemy_vision]
            print_3d_list(board_)
            cur_board_in_enemy_vision = board_P2_in_enemy_vision
        if n == 2:
            enemy_board = board_P1
            board_ = [board_P1_in_enemy_vision,board_P2]
            print_3d_list(board_)
            cur_board_in_enemy_vision = board_P1_in_enemy_vision

        print_player_turn_to_strike(n)
        print_choose_target_coordinates()
        coordinates_input = input().lower().strip()
        #Let's first check for inputs if they are valid or not
        #Check if enough arguments are given
        if len(coordinates_input.split()) != 2:
            print_incorrect_input_format()
            continue

        (x_cor,y_cor) = coordinates_input.split()
        #Check if the coordinates are integers
        try:
            x_cor = int(x_cor)
            y_cor = int(y_cor)
        except:
            print_incorrect_input_format()
            continue

        #Check if the coordinates are inside the board
        if not (0<x_cor<=10 and 0<y_cor<=10):
            print_incorrect_coordinates()
            continue
        #Check if the tile is already struck
        if enemy_board[y_cor-1][x_cor-1] in ['!','O']:
            print_tile_already_struck()
            continue

        #Inputs are checked. Let's begin the attack phase!

        #If it's a miss
        if enemy_board[y_cor-1][x_cor-1] != "#":
            print_miss()
            cur_board_in_enemy_vision[y_cor-1][x_cor-1] = 'O'
            enemy_board[y_cor-1][x_cor-1] = 'O'

            n= (n)%2+1 # if n ==1 it's 2, if n==2 it's 1
            while True:
                print_type_done_to_yield(n)
                yield_input = input().lower().strip()
                if yield_input == 'done':
                    break
            continue

        #If it's hit!!! KABOOOOMM!
        if enemy_board[y_cor-1][x_cor-1] == "#":
            print_hit()
            cur_board_in_enemy_vision[y_cor-1][x_cor-1] = '!'
            enemy_board[y_cor-1][x_cor-1] = '!'
            continue


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

