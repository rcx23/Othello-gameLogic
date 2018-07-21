#Project 4 Ryan Cox ID# 31953949

import project4classes as classes

def main_runner():
    print("FULL")

    rows = _row_input()
    columns = _col_input()
    turn = _move_input()
    how_won = _how_won_input()
    board = _create_board(rows)

    gamestate = classes.Othello(rows, columns, turn, how_won, board)

    while classes.Othello.game_over(gamestate) == True:
        print(classes.Othello.score(gamestate))
        print_board(gamestate)
        print("Turn: ", turn)

        if turn == 'W':
            turn = 'B'
        else:
            turn = 'W'

        turn_test = classes.Othello.valid_moves(gamestate)

        if turn_test != []:
            gamestate.board = classes.Othello.make_move(gamestate)

        gamestate.turn = turn
        gamestate = classes.Othello(rows, columns, turn, how_won, board)

    print(classes.Othello.score(gamestate))
    print_board(gamestate)
    print(classes.Othello.game_over_output(gamestate))
    

##### PRIVATE FUNCTIONS #####
def _row_input() -> int:
    ''' handles the row input '''
    while True:
        row_input = int(input())
        if row_input >= 4 and row_input <= 16:
            return row_input

def _col_input() -> int:
    ''' handles the col input '''
    while True:
        col_input = int(input())
        if col_input >= 4 and col_input <= 16:
            return col_input

def _move_input() -> str:
    ''' handles the move input '''
    while True:
        move_input = input()
        if move_input == 'B' or move_input == 'W':
            return move_input

def _how_won_input() -> str:
    ''' handles how the game is won '''
    while True:
        how_won_input = input()
        if how_won_input == '>' or how_won_input == '<':
            return how_won_input

##### BOARD FUNCTIONS #####

def _create_board(rows: int) -> [[list]]:
    ''' creates the game board '''
    game_board = []

    for each in range(rows):
        user_input = str(input())
        game_board.append(user_input.split())

    return game_board

def print_board(gamestate: classes.Othello) -> None:
    ''' prints the game board'''
    board = gamestate.board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'W':
                print('W ', end = '')
            elif board[row][col] == 'B':
                print('B ', end = '')
            elif board[row][col] == '.':
                print('. ', end = '')
            else:
                pass
        print()




if __name__ == '__main__':
    main_runner()
