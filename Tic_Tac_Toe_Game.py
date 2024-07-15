PLAYER1_NAME = None
PLAYER2_NAME = None

TTarr = {
    1 : ' ',
    2 : ' ',
    3 : ' ',
    4 : ' ',
    5 : ' ',
    6 : ' ',
    7 : ' ',
    8 : ' ',
    9 : ' '
}

FollowUpPositions= {
    1 : False,
    2 : False,
    3 : False,
    4 : False,
    5 : False,
    6 : False,
    7 : False,
    8 : False,
    9 : False
}

Avail_Positions = []

PLAYERS_SYMBOL = dict()

PLAYER1_TURN = False
PLAYER2_TURN = False

choice = ''

def Set_Players():
    global PLAYER1_NAME
    global PLAYER2_NAME
    print('###### Enter Player names Here ######')

    while True:

        PLAYER1_NAME = input('$-enter Player-1 Name?\n')

        if not PLAYER1_NAME:
            print('Player-1 name Invalid. so,Please enter valid Name.')
        else:
            break

    while True:

        PLAYER2_NAME = input('$-enter Player-2 Name?\n')

        if not PLAYER2_NAME:
            print('Player-2 name Invalid. so,Please enter valid Name.')
        else:
            break

def Display_Symbols():
    print('******** Registered Symbols *********')

    print('  \tPlayer_Name\t \tSymbol')
    print(f'1.\t{PLAYER1_NAME}\t-\t{PLAYERS_SYMBOL[PLAYER1_NAME]}')
    print(f'2.\t{PLAYER2_NAME}\t-\t{PLAYERS_SYMBOL[PLAYER2_NAME]}')

def Set_Symbols():
    global PLAYERS_SYMBOL

    allowedSymbols = ['X', 'O']

    print('******* Choose Your Symbol ********')

    isValideSymbol = True

    while isValideSymbol:

        Player1_symbol = input(f'Hey {PLAYER1_NAME}, Choose Your Symbol? (X/O)')

        if Player1_symbol not in allowedSymbols:
            print('Please Enter a Valid Input.')
        else:
            break
    allowedSymbols.remove(Player1_symbol)

    while isValideSymbol:
        Player2_symbol = input(f'Hey {PLAYER2_NAME}, Choose Your Symbol? (X/O)')

        if Player2_symbol not in ['X', 'O']:
            print('Please Enter a Valid Input.')
        else:
            break

    PLAYERS_SYMBOL[PLAYER1_NAME] = Player1_symbol
    PLAYERS_SYMBOL[PLAYER2_NAME] = Player2_symbol

def Available_Positions():
    global Avail_Positions
    Avail_Positions = []

    for i in FollowUpPositions:
        if not FollowUpPositions[i]:
            Avail_Positions.append(i)


def setDataToGame(Position):
    global PLAYER1_TURN
    global PLAYER2_TURN
    if PLAYER1_TURN and not FollowUpPositions[Position]:
        TTarr[Position] = PLAYERS_SYMBOL[PLAYER1_NAME]
        FollowUpPositions[Position] = True
        PLAYER1_TURN = False

    if PLAYER2_TURN and not FollowUpPositions[Position]:
        TTarr[Position] = PLAYERS_SYMBOL[PLAYER2_NAME]
        FollowUpPositions[Position] = True
        PLAYER2_TURN = False

def display_data(TTarr):
    print('****** Updated Data ******')

    print('-------------------\n'
          f'|  {TTarr[1]}  |  {TTarr[2]}  |  {TTarr[3]}  |\n'
          '-------------------\n'
          f'|  {TTarr[4]}  |  {TTarr[5]}  |  {TTarr[6]}  |\n'
          '-------------------\n'
          f'|  {TTarr[7]}  |  {TTarr[8]}  |  {TTarr[9]}  |\n'
          '-------------------\n')

def validate_input():
    global Avail_Positions,choice

    if choice.isnumeric():
        choice = int(choice)
        if choice in Avail_Positions:
            return True
        else:
            print('The Position is Unavailable, give a valid position')
    else:
        print('Other datatypes are not allowed.Only INTEGER Datatype is Allowed, Please give a valid input.')

def FindPlayer(symbol):
    if symbol == PLAYERS_SYMBOL[PLAYER1_NAME]:
        return PLAYER1_NAME
    else:
        return PLAYER2_NAME

def winnerDesision():
    global FollowUpPositions

    if TTarr[1] == TTarr[2] and TTarr[2] == TTarr[3] and (TTarr[1] == 'X' or TTarr[1] == 'O'):
        symbol = TTarr[1]
        winner = FindPlayer(symbol)
        return winner
    elif TTarr[4] == TTarr[5] and TTarr[5] == TTarr[6] and (TTarr[4] == 'X' or TTarr[4] == 'O'):
        symbol = TTarr[4]
        winner = FindPlayer(symbol)
        return winner
    elif TTarr[7] == TTarr[8] and TTarr[8] == TTarr[9] and (TTarr[7] == 'X' or TTarr[7] == 'O'):
        symbol = TTarr[7]
        winner = FindPlayer(symbol)
        return winner
    elif TTarr[1] == TTarr[4] and TTarr[4] == TTarr[7] and (TTarr[1] == 'X' or TTarr[1] == 'O'):
        symbol = TTarr[1]
        winner = FindPlayer(symbol)
        return winner
    elif TTarr[2] == TTarr[5] and TTarr[5] == TTarr[8] and (TTarr[2] == 'X' or TTarr[2] == 'O'):
        symbol = TTarr[2]
        winner = FindPlayer(symbol)
        return winner
    elif TTarr[3] == TTarr[6] and TTarr[6] == TTarr[9] and (TTarr[3] == 'X' or TTarr[3] == 'O'):
        symbol = TTarr[3]
        winner = FindPlayer(symbol)
        return winner
    elif TTarr[1] == TTarr[5] and TTarr[5] == TTarr[9] and (TTarr[1] == 'X' or TTarr[1] == 'O'):
        symbol = TTarr[9]
        winner = FindPlayer(symbol)
        return winner
    elif TTarr[3] == TTarr[5] and TTarr[5] == TTarr[7] and (TTarr[3] == 'X' or TTarr[3] == 'O'):
        symbol = TTarr[3]
        winner = FindPlayer(symbol)
        return winner
    return None

def DisplayWinner(winner):
    if winner:
        print(f'Congratulations {winner}! You are the Winner!')
        print('*********** Game Over ************')
        return True
    return False
def main():
    global PLAYER1_TURN
    global PLAYER2_TURN
    global choice
    print('****** Tic Tac Game ******')
    print('Game Structure and It Positions:')
    print('-------------------\n'
          '|  1  |  2  |  3  |\n'
          '-------------------\n'
          '|  4  |  5  |  6  |\n'
          '-------------------\n'
          '|  7  |  8  |  9  |\n'
          '-------------------\n')

    display_data(TTarr)

    Set_Players()
    print('Your Names Successfully Registered.')

    Set_Symbols()
    print('Symbols Successfully Registered with Your Name.')
    Display_Symbols()

    while True:
        Available_Positions()
        if not Avail_Positions:
            print('Match Draw!')
            break
        else:
            print(f'You are able to place only in these Positions: {Avail_Positions}')

        while not PLAYER1_TURN:
            print(f'Hey {PLAYER1_NAME}, Choose one Position to Place the symbol: ')
            choice = input()
            PLAYER1_TURN = validate_input()

        setDataToGame(choice)
        PLAYER1_TURN = False
        display_data(TTarr)
        winner = winnerDesision()

        if DisplayWinner(winner):break

        Available_Positions()
        if not Avail_Positions:
            print('Match Draw!')
            break
        else:
            print(f'You are able to place only in these Positions: {Avail_Positions}')

        while not PLAYER2_TURN:
            print(f'Hey {PLAYER2_NAME}, Choose one Position to Place the symbol: ')
            choice = input()
            PLAYER2_TURN = validate_input()

        setDataToGame(choice)
        PLAYER2_TURN = False
        display_data(TTarr)
        winner = winnerDesision()

        if DisplayWinner(winner):break

if __name__ == '__main__':
    main()
