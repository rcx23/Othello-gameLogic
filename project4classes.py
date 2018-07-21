#Project 4 classes

class GameError(Exception):
    pass

class Othello:
    def __init__ (self, rows: int, columns: int, turn_first: str, how_its_won: str, board: [[list]]):
        self.row = rows
        self.col = columns
        self.turn = turn_first
        self.how_won = how_its_won
        self.board = board

    def score(self) -> str:
        ''' returns count of each turn '''
        white = 0
        black = 0
        board = self._board()
        rows = self._row()
        columns = self._col()

        for each in range(rows):
            for other in range(columns):
                if board[other][each] == 'W':
                    white += 1
                elif board[other][each] == 'B':
                    black += 1
                else:
                    pass
        return "B: {}  W: {}".format(black,white)

    def change_turn(self):
        ''' changes the turn '''
        self.turn = self._change_turn()
    
    def _change_turn(self):
        ''' reads current turn and  '''
        current_turn = self.turn

        if turn == 'W':
            print('B')
            return 'B'
        else:
            print('W')
            return 'W'

    def on_board(self, row: int, col: int) -> bool:
        ''' tests if a move is viable '''
        if row >= 0 and row <= self._row() and col >= 0 and col <= self._col():
            return True
        else:
            return False

    def empty_spot(self, row: int, col:int):
        ''' tests if a spot is empty '''
        board = self._board()

        if board[row][col] == '.':
            return True
        else:
            return False

    ##### Moves #####

    def make_move(self):
        ''' allows the current player to make a turn '''
        possible_moves = self.valid_moves()
        flip = []
        test = [[0,1],[1,0],[0,-1],[-1,0],[-1,1],[1,-1],[-1,-1],[1,1]]
        turn = self.turn
        other_turn = ''
        if turn == 'B':
            other_turn = 'W'
        else:
            other_turn = 'B'
            
        board = self._board()
        rows = self._row()
        cols = self._col()
        try:           
            moves = input()
            moves = moves.split()
            moves[0] = int(moves[0])
            moves[1] = int(moves[1])
            moves[0] -= 1
            moves[1] -= 1
            row_move = moves[0]
            col_move = moves[1]

            move = [row_move, col_move]

            if move in possible_moves:
                print("VALID")
                board[row_move][col_move] = turn
                for k in test:
                    temp = []
                    r = row_move
                    c = col_move
                    r += k[0]
                    c += k[1]
                    if r >= 0 and r < self.row and c >= 0 and c < self.col:
                        if board[r][c] == other_turn:
                            while board[r][c] == other_turn and r >= 0 and r < self.row and c >= 0 and c < self.col:
                                temp.append([r, c])
                                r += k[0]
                                c += k[1]
                                if r < 0 and r >= self.row and c < 0 and c >= self.col:
                                    r -= k[0]
                                    c -= k[1]
                                    break
                            if board[r][c] == turn:
                                for each in temp:
                                    flip.append(each)
                            else:
                                temp = []
                    else:
                        pass
                
        except:
            print("INVALID")
        else:
            for r,c in flip:
                board[r][c] = turn


                

    def valid_moves(self) -> list:
        ''' returns a list of valid moves for the current player '''
        moves = []
        test = [[0,1],[1,0],[0,-1],[-1,0],[-1,1],[1,-1],[-1,-1],[1,1]]
        turn = self.turn
        other_turn = ''
        if turn == 'B':
            other_turn = 'W'
        else:
            other_turn = 'B'
        board = self._board()
        rows = self._row()
        cols = self._col()

        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == '.':
                    for k in test:
                        r = i
                        c = j
                        r += k[0]
                        c += k[1]
                        if r > 0 and r < self.row and c > 0 and c < self.col:
                            if board[r][c] == other_turn:
                                while board[r][c] == other_turn and r >= 0 and r < self.row-1 and c >= 0 and c < self.col-1:
                                    r += k[0]
                                    c += k[1]
                                if board[r][c] == turn:
                                    moves.append([i,j])
                                elif board[r][c] != turn:
                                    pass
                            elif board != other_turn:
                                pass
                        else:
                            pass
                else:
                    pass

        return moves

        
    ##### Game Over #####
    def game_over(self) -> bool:
        ''' checks to see if the game is over '''
        moves_left = 0
        board = self._board()

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    moves_left += 1
                else:
                    pass
        if moves_left > 0:
            return True
        else:
            return False
        


    def game_over_output(self) -> str:
        ''' returns the winner '''
        board = self._board()
        black = 0
        white = 0
        how_won = self._how_won()

        for i in range(self._row()):
            for j in range(self._col()):
                if board[i][j] == 'W':
                    white += 1
                elif board[i][j] == 'B':
                    black += 1
                else:
                    pass
        if how_won == '>':
            if black > white:
                return 'WINNER: B'
            elif black < white:
                return 'WINNER: W'
            else:
                return 'WINNER: NONE'
        elif how_won == '<':
            if black < white:
                return 'WINNER: B'
            elif black > white:
                return 'WINNER: W'
            else:
                return 'WINNER: NONE'
                

    ##### Private Functions to call variable #####
    def _row(self) -> int:
        return self.row

    def _col(self) -> int:
        return self.col

    def _turn(self) -> str:
        return self.turn

    def _how_won(self) -> str:
        return self.how_won

    def _board(self) -> [[list]]:
        return self.board
