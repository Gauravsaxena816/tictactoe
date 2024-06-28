class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to store 9 spaces
        self.current_winner = None  # Keep track of the winner!

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(state, player):
    max_player = 'O'
    other_player = 'X' if player == 'O' else 'O'

    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (state.board.count(' ') + 1) if other_player == max_player else -1 * (state.board.count(' ') + 1)}
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    best = {'position': None, 'score': float('-inf') if player == max_player else float('inf')}
    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax(state, other_player)
        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score

    return best
