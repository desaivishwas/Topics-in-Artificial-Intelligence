

#
# pikachu.py : Play the game of Pikachu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
# Ayush Sanghavi : sanghavi     Vighnesh Kolhatkar: vkolhatk    Vishwas Desai: visdesai
# Based on skeleton code by D. Crandall, March 2021
#

import sys
import time
from copy import deepcopy

def board_to_string(board, N):
    return "\n".join(board[i:i + N] for i in range(0, len(board), N))


# __________________________________________ converting string to matrix board _______________________________________________________

# --------------- The following function was referred from "https://www.geeksforgeeks.org/python-convert-strings-to-character-matrix/" -------------

def convert_to_board(board, N):
    # slicing strings
    temp = [board[i: i + N] for i in range(0, len(board), N)]

    # conversion to list of characters
    res = [list(char) for char in temp]

    # return the result
    return res

# ---------------------------------------------------- Referred code ends here ---------------------------------


# __________________________________________ converting matrix board to string _______________________________________________________


def convert_to_string(board):
    return ''.join(str(char) for j in board for char in j)


# __________________________________________ converting to Pikachu _______________________________________________________

def is_pikachu(player, r, N):
    if player == 'w':
        if r == N-1:
            return True
        else:
            return False

    elif player == 'b':
        if r == 0:
            return True
        else:
            return False


# __________________________________________ BLACK PIKACHU & PICHU _______________________________________________________


# To figure out the moves function for the Pichus and the Piakchus, we had a discussion at an abstract level with ssumbad-mivakh-vbenadik group

# Black PIKACHU
def valid_moves_B(board, N):
    boards_B = []
    for r in range(0, N):
        for c in range(0, N):

            if board[r][c] == 'B':
                # from current row to the first row

                if r!=0:
                    is_opponent = False
                    for i in range(r, -1, -1):
                        # Jump spaces
                        if board[i - 1][c] == '.':
                            board_new = deepcopy(board)
                            board_new[i][c] = '.'
                            board_new[i - 1][c] = 'B'
                            boards_B.append(board_new)

                        # Opponent jump
                        if not is_opponent and (board[i - 1][c] == 'w' or board[i - 1][c] == 'W'):
                            if board[i - 2][c] == '.':
                                board_new = deepcopy(board)
                                board_new[i][c] = '.'
                                board_new[i - 1][c] = '.'
                                board_new[i - 2][c] = 'B'
                                is_opponent = True
                                boards_B.append(board_new)

                # from current row to the last row

                if r<N-1:
                    is_opponent = False
                    for j in range(r + 1, N-2):
                        # Jump spaces
                        if board[j + 1][c] == '.':
                            board_new = deepcopy(board)
                            board_new[j][c] = '.'
                            board_new[j + 1][c] = 'B'
                            boards_B.append(board_new)

                        # Opponent jump
                        if not is_opponent and (board[j + 1][c] == 'w' or board[j + 1][c] == 'W'):
                            if board[j + 2][c] == '.':
                                board_new = deepcopy(board)
                                board_new[j][c] = '.'
                                board_new[j + 1][c] = '.'
                                board_new[j + 2][c] = 'B'
                                is_opponent = True
                                boards_B.append(board_new)

                # from current column to the first column
                if c!=0:
                    is_opponent = False
                    for k in range(c, -1, -1):
                        # jump spaces
                        if board[r][k - 1] == '.':
                            board_new = deepcopy(board)
                            board_new[r][k] = '.'
                            board_new[r][k - 1] = 'B'
                            boards_B.append(board_new)

                        # Opponent jump
                        if not is_opponent and (board[r][k - 1] == 'w' or board[r][k - 1] == 'W'):
                            if board[r][k - 1] == '.':
                                board_new = deepcopy(board)
                                board_new[r][k] = '.'
                                board_new[r][k - 1] = '.'
                                board_new[r][k - 2] = 'B'
                                is_opponent = True
                                boards_B.append(board_new)

                # from current column to last column
                if c!=N-1:
                    is_opponent = False
                    for k in range(c, N-2):
                        # jump spaces
                        if board[r][k + 1] == '.':
                            board_new = deepcopy(board)
                            board_new[r][k] = '.'
                            board_new[r][k + 1] = 'B'
                            boards_B.append(board_new)

                        # Opponent jump
                        if not is_opponent and (board[r][k - 1] == 'w' or board[r][k - 1] == 'W'):
                            if board[r][k - 1] == '.':
                                board_new = deepcopy(board)
                                board_new[r][k] = '.'
                                board_new[r][k + 1] = '.'
                                board_new[r][k + 2] = 'B'
                                is_opponent = True
                                boards_B.append(board_new)

    #print(boards_B)
    return boards_B


# Black PICHU

def valid_moves_b(board, N):
    # pika = False
    boards_b = []
    for r in range(0, N):
        # if pika:
        # break
        for c in range(0, N):
            if board[r][c] == 'b':
                # Moving forward, left, right if squares are empty
                if board[r - 1][c] == ".":
                    if is_pikachu('b', r - 1, N):
                        board_new = deepcopy(board)
                        board_new[r][c] = '.'
                        board_new[r - 1][c] = 'B'
                        boards_b.append(board_new)
                    else:
                        board_new = deepcopy(board)
                        board_new[r][c] = '.'
                        board_new[r - 1][c] = 'b'
                        boards_b.append(board_new)

                if c!=0 and board[r][c - 1] == ".":
                    board_new = deepcopy(board)
                    board_new[r][c] = '.'
                    board_new[r][c - 1] = 'b'
                    boards_b.append(board_new)

                if c!=N-1 and board[r][c + 1] == ".":
                    board_new = deepcopy(board)
                    board_new[r][c] = '.'
                    board_new[r][c + 1] = 'b'
                    boards_b.append(board_new)

                # JUMP
                if board[r - 1][c] == "w" or board[r - 1][c] == 'W':
                    if board[r - 2][c] == ".":
                        if is_pikachu('b', r - 1, N):
                            board_new = deepcopy(board)
                            board_new[r][c] = '.'
                            board_new[r - 1][c] = '.'
                            board_new[r - 2][c] = 'B'
                            boards_b.append(board_new)
                        else:
                            board_new = deepcopy(board)
                            board_new[r][c] = '.'
                            board_new[r - 1][c] = '.'
                            board_new[r - 2][c] = 'b'
                            boards_b.append(board_new)

                if c!=N-1 and c!=N-2 and (board[r][c + 1] == "w" or board[r][c + 1] == 'W'):
                    if board[r][c + 2] == ".":
                        board_new = deepcopy(board)
                        board_new[r][c] = '.'
                        board_new[r][c + 1] = '.'
                        board_new[r][c + 2] = 'b'
                        boards_b.append(board_new)

                if c!=0 and c!=1 and (board[r][c - 1] == "w" or board[r][c - 1] == 'W'):
                    if board[r][c - 2] == ".":
                        board_new = deepcopy(board)
                        board_new[r][c] = '.'
                        board_new[r][c - 1] = '.'
                        board_new[r][c - 2] = 'b'
                        boards_b.append(board_new)

    #print(boards_b)
    return boards_b


# __________________________________________ WHITE PIKACHU & PICHU ________________________________________________________
# WHITE PIKACHU
def valid_moves_W(board, N):
    # valid_move_W = []
    boards_W = []

    for r in range(0, N):
        for c in range(0, N):
            if board[r][c] == "W":
                is_opponent = False
                # FORWARDS
                if r!=N-1:
                    for i in range(r, N-2):
                        if board[i + 1][c] == ".":
                            board_new = deepcopy(board)
                            board_new[i][c] = "."
                            board_new[i + 1][c] = "W"
                            boards_W.append(board_new)
                        # JUMP
                        if not is_opponent and (board[i + 1][c] == "B" or board[i + 1][c] == "b"):
                            if board[i + 2][c] == ".":
                                board_new = deepcopy(board)
                                board_new[i][c] = "."
                                board_new[i + 1][c] = "."
                                board_new[i + 2][c] = "W"
                                is_opponent = True
                                boards_W.append(board_new)
                # BACKWARDS
                is_opponent = False
                if r!=0:
                    for j in range(r - 1, -1, -1):
                        if board[j - 1][c] == ".":
                            board_new = deepcopy(board)
                            board_new[j][c] = "."
                            board_new[j - 1][c] = "W"
                            boards_W.append(board_new)
                        if not is_opponent and (board[j - 1][c] == "B" or board[j - 1][c] == "b"):
                            if board[j - 2][c] == ".":
                                board_new = deepcopy(board)
                                board_new[j][c] = "."
                                board_new[j - 1][c] = "."
                                board_new[j - 2][c] = "W"
                                is_opponent = True
                                boards_W.append(board_new)
                # RIGHT
                is_opponent = False
                if c!=N-1:
                    for k in range(c + 1, N-2):
                        if board[k + 1][c] == ".":
                            board_new = deepcopy(board)
                            board_new[k][c] = "."
                            board_new[k - 1][c] = "W"
                            boards_W.append(board_new)
                        if not is_opponent and (board[k + 1][c] == "B" or board[k + 1][c] == "b"):
                            if board[k - 2][c] == ".":
                                board_new = deepcopy(board)
                                board_new[k][c] = "."
                                board_new[k + 1][c] = "."
                                board_new[k + 2][c] = "W"
                                is_opponent = True
                                boards_W.append(board_new)
                # LEFT
                is_opponent = False
                if c!=0:
                    for l in range(c, -1, -1):
                        if board[l - 1][c] == ".":
                            board_new = deepcopy(board)
                            board_new[l][c] = "."
                            board_new[l - 1][c] = "W"
                            boards_W.append(board_new)
                        if not is_opponent and (board[l - 1][c] == "B" or board[l + 1][c] == "b"):
                            if board[k - 2][c] == ".":
                                board_new = deepcopy(board)
                                board_new[l][c] = "."
                                board_new[l - 1][c] = "."
                                board_new[l - 2][c] = "W"
                                is_opponent = True
                                boards_W.append(board_new)

    #print(boards_W)
    return boards_W


# WHITE PICHU 

def valid_moves_w(board, N):
    #

    # valid_move_w = []
    boards_w = []
    # eliminate_b = []
    # pika = False
    for r in range(0, N):
        for c in range(0, N):
            # if pika:
            # break
            # # Moving forward, left, right if squares are empty
            if board[r][c] == 'w':
                if board[r + 1][c] == ".":
                    if is_pikachu('w', r + 1, N):
                        board_new = deepcopy(board)
                        board_new[r][c] = "."
                        board_new[r + 1][c] = "W"
                        boards_w.append(board_new)
                    else:
                        board_new = deepcopy(board)
                        board_new[r][c] = "."
                        board_new[r + 1][c] = "w"
                        boards_w.append(board_new)

                if  c!= 0 and board[r][c - 1] == "." :
                    board_new = deepcopy(board)
                    board_new[r][c] = "."
                    board_new[r][c - 1] = "w"
                    boards_w.append(board_new)

                if c!= N-1 and board[r][c + 1] == ".":
                    board_new = deepcopy(board)
                    board_new[r][c] = "."
                    board_new[r][c + 1] = "w"
                    boards_w.append(board_new)

                # JUMP
                if board[r + 1][c] == "b" or board[r + 1][c] == 'B':
                    if board[r + 2][c] == ".":
                        if is_pikachu('w', r + 1, N):
                            board_new = deepcopy(board)
                            board_new[r][c] = "."
                            board_new[r + 1][c] = "."
                            board_new[r + 2][c] = "W"
                            boards_w.append(board_new)
                        else:
                            board_new = deepcopy(board)
                            board_new[r][c] = "."
                            board_new[r + 1][c] = "."
                            board_new[r + 2][c] = "w"
                            boards_w.append(board_new)

                if c!= N-1 and c!= N-2 and (board[r][c + 1] == "b" or board[r][c + 1] == 'B'):
                    if board[r][c + 2] == ".":
                        board_new = deepcopy(board)
                        board_new[r][c] = "."
                        board_new[r][c + 1] = "."
                        board_new[r][c + 2] = "w"
                        boards_w.append(board_new)

                if c!=0 and c!=1 and (board[r][c - 1] == "b" or board[r][c - 1] == 'B'):
                    if board[r][c - 2] == ".":
                        board_new = deepcopy(board)
                        board_new[r][c] = "."
                        board_new[r][c - 1] = "."
                        board_new[r][c - 2] = "w"
                        boards_w.append(board_new)

    #print(convert_to_string(boards_w))
    return boards_w


# __________________________________________Successors_______________________________________________________


def successors(board, player):
    N = len(board)
    if player == 'w':
        return valid_moves_w(board, N) + valid_moves_W(board, N)
    elif player == 'b':
        return valid_moves_b(board, N) + valid_moves_B(board, N)


# __________________________________________ Evaluation function _______________________________________________________


def eval_func(board, player1_max):
    count_w = 0
    count_W = 0
    count_b = 0
    count_B = 0
    N = len(board)  # N * N matrix

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'b':
                count_b += 1
            elif board[i][j] == 'w':
                count_w += 1
            elif board[i][j] == "B":
                count_B += 1
            elif board[i][j] == "W":
                count_W += 1

    if player1_max == "w":
        return 7 * (count_w - count_b) + 35 * (count_W - count_B)
    else:
        return 7 * (count_b - count_w) + 35 * (count_B - count_W)


# --------------------------CHECK GOAL ------------------------------
def is_goal_state(board, player1_max):
    count_w = 0
    count_b = 0
    count_W = 0
    count_B = 0

    # for calculating the number of white and black pichus and pikachus on the board
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'b':
                count_b += 1
            elif board[i][j] == 'w':
                count_w += 1
            elif board[i][j] == "B":
                count_B += 1
            elif board[i][j] == "W":
                count_W += 1

    if (count_w + count_W) == 0 and player1_max == 'w':
        return True
    elif (count_b + count_B) == 0 and player1_max == 'b':
        return True
    else:
        return False


# ________________________________MINIMAX_____________________________________

# --------- The following function was referred from "https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/" and discussed with Ajinkya Pawale --------------------

def find_min(board, player1_max, player2_min, alpha, beta, depth):
    best_move = None

    if depth == 0 or is_goal_state(board, player1_max):
        return board, eval_func(board, player1_max)

    min_value = float('inf')

    for s in successors(board, player2_min):
        v = find_max(s, player1_max, player2_min, alpha, beta, depth - 1)[1]

        if v < min_value:
            min_value = v
            best_move = s

        if min_value < beta:
            beta = min_value

        if min_value <= alpha:
            return (best_move, min_value)

    return (best_move, min_value)


def find_max(board, player1_max, player2_min, alpha, beta, depth):
    best_move = None

    if depth == 0 or is_goal_state(board, player1_max):
        return (board, eval_func(board, player2_min))

    max_value = float('-inf')

    for s in successors(board, player1_max):
        v = find_min(s, player1_max, player2_min, alpha, beta, depth - 1)[1]

        if v > max_value:
            max_value = v
            best_move = s

        if max_value > alpha:
            alpha = max_value

        if max_value >= beta:
            return (best_move, max_value)

    return (best_move, max_value)


def alpha_beta(board, player1_max, player2_min, depth):
    alpha = float('-inf')
    beta = float('inf')
    max_value = float('-inf')
    best_move = None

    for s in successors(board, player1_max):
        v = find_min(s, player1_max, player2_min, alpha, beta, depth)[1]
        if v > max_value:
            max_value = v
            best_move = s

    return best_move

# -------------------------------- Referred code ends here ---------------------------------

def find_best_move(board, player, timelimit, depth, N):
    board = convert_to_board(board, N)
    if player == "w":
        player1_max = "w"
        player2_min = "b"
    else:
        player1_max = "b"
        player2_min = "w"

    best_board = alpha_beta(board, player1_max, player2_min, depth)
    return convert_to_string(best_board)



if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: pikachu.py N player board timelimit")

    (_, N, player, board, timelimit) = sys.argv
    N = int(N)
    timelimit = int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N * N or 0 in [c in "wb.WB" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for i in range(3,4):
        depth = i
        new_board = find_best_move(board, player, timelimit, depth, N)
        print(new_board)

