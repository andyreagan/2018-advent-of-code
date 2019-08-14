# MassMutual Python month of Code
# My solution for Emad's problem
#
# 2019-08-14
# Andy Reagan

valid_board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
invalid_board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]



def get_board_row(board: list, i: int) -> list:
    return board[i]


def get_board_column(board: list, i: int) -> list:
    return [board[j][i] for j in range(len(board))]


def get_board_cell(board: list, i: int) -> list:
    '''
    1 -> 1, 1
    2 -> 2, 1
    3 -> 3, 1
    4 -> 1, 2
    5 -> 2, 2
    ...
    '''
    return [board[(j % 3) + ((i % 3) * 3)][(j // 3) + ((i // 3) * 3)] for j in range(len(board))]


def check_list(l: list) -> bool:
    numbers = [int(x) for x in l if x != "."]
    return len(set(numbers)) == len(numbers)


def is_valid_board(board: list) -> bool:
    return (
        all(check_list(get_board_row(board, i)) for i in range(len(board))) &
        all(check_list(get_board_column(board, i)) for i in range(len(board))) &
        all(check_list(get_board_cell(board, i)) for i in range(len(board)))
    )

is_valid_board(valid_board)
is_valid_board(invalid_board)
