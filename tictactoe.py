"""
Tic Tac Toe Player
"""

import math,random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x_count += 1
            if board[i][j] == 'O':
                o_count += 1
    # print('o', o_count)
    # print('x',x_count)
    if x_count == o_count:
        return 'X'
    elif x_count > o_count:
        return 'O'
    else:
        return 'X'
    
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                moves.add((row,col))
    
    return moves
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # possible error caught in case of invalid action
    # print(type(action))
    i = action[0]
    j = action[1]
    new_board = [row[:] for row in board]

    if new_board[i][j] is None:
        new_board[i][j] = player(new_board)
    return new_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # print(board)
    for row in range(3):
        for col in range(3):
            # print(board[row][col])
            # print(type(board[row][col]))
            if  type(board[row][col]) != type(EMPTY):
                if row == 0:
                    if col == 0:
                        #diagonal
                        if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2]:
                            return board[row][col]
                    
                    if col == 2:
                        if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2]:
                            return board[row][col]
                    #vertical
                    if board[row][col] == board[row + 1][col] == board[row + 2][col]:
                        return board[row][col]
                if col == 0:
                    #horizontal
                    if board[row][col] == board[row][col + 1] == board[row][col + 2]:
                        return board[row][col]

    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    none_count = 0
    for row in range(3):
        for col in  range(3):
            if board[row][col] == None:
                none_count += 1

    if  none_count == 0 or winner(board) is not None:
        return True
    return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    # print(type(win))
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    'X' Player is trying to maximise the score, 'O' Player is trying to minimise it
    """

    

    def max_player(board, best_min = 10):
        #global actions_explored

        # If the game is over, return board value
        if terminal(board):
            return (utility(board), None)

        # Else pick the action giving the max value when min_player plays optimally
        value = -10
        best_action = None


        # Get set of actions and then select a random one until list is empty:
        action_set = actions(board)

        while len(action_set) > 0:
            action = random.choice(tuple(action_set))
            action_set.remove(action)

        # A-B Pruning skips calls to min_player if lower result already found:
            if best_min <= value:
                break

        # actions_explored += 1
        min_player_result = min_player(result(board, action), value)
        if min_player_result[0] > value:
          best_action = action
          value = min_player_result[0]

        return (value, best_action)


    def min_player(board, best_max = -10):

        # global actions_explored

        # If the game is over, return board value
        if terminal(board):
            return (utility(board), None)

        # Else pick the action giving the min value when max_player plays optimally
        value = 10
        best_action = None

        # Get set of actions and then select a random one until list is empty:
        action_set = actions(board)

        while len(action_set) > 0:
            action = random.choice(tuple(action_set))
            action_set.remove(action)

        # A-B Pruning skips calls to max_player if higher result already found:
        # if best_max >= value:
        #   break

        # actions_explored += 1
        max_player_result = max_player(result(board, action), value)
        if max_player_result[0] < value:
            best_action = action
            value = max_player_result[0]

        return (value, best_action)


    # If the board is terminal, return None:
    if terminal(board):
        return None

    if player(board) == 'X':
    #print('AI is exploring possible actions...')
        best_move = max_player(board)[1]
    #print('Actions explored by AI: ', actions_explored)
        return best_move
    else:
    #print('AI is exploring possible actions...')
        best_move = min_player(board)[1]
    #   print('Actions explored by AI: ', actions_explored)
        return best_move


