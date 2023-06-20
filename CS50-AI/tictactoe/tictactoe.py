"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0
    
    for row in board:
        for tile in row:
            if tile == "X":
                xCount += 1
            elif tile == "O":
                oCount += 1
    
    if x_count == o_count:
        return "X"
    else:
        return "O"


def actions(board):
    actions = set()

    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    curr_player = player(board)
    board_copy = copy.deepcopy(board)

    board_copy[action[0]][action[1]] = curr_player

    return board_copy

def win_types(board):
  wins = [
    board[0], board[1], board[2], [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    [board[0][0], board[1][1], board[2][2]],
    [board[2][0], board[1][1], board[0][2]]
  ]
  return wins


def winner(board):
    for win in win_types(board):
        if not ((None in win) or ("O" in win)):
            return "X"
        elif not ((None in win) or ("X" in win)):
            return "O"
    return None


def terminal(board):
    over = True

    if winner(board) == None:
        for row in board:
            for tile in row:
                if tile == None:
                    over = False

    return over


def utility(board):
    util_dict = {
  "X": 1,
  "O": -1,
  None: 0
}
    return util_dict[winner(board)]




class Move():
        def __init__(self, action):
            self.value = 0
            self.action = action

        # def calc_value(self):
            




def minimax(board):
    moves = []
    for action in actions(board):
        moves.append(Move(action))
    

