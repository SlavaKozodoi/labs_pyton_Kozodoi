from random import randrange

def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    move = None
    while move not in range(1, 10):
        try:
            move = int(input("Введіть свій хід (1-9): "))
            if move not in range(1, 10):
                print("Неправильне число. Спробуйте ще раз.")
            else:
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] in ['X', 'O']:
                    print("Ця клітинка вже зайнята. Виберіть іншу.")
                    move = None
                else:
                    board[row][col] = 'O'
        except ValueError:
            print("Будь ласка, введіть число від 1 до 9.")

def make_list_of_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['X', 'O']]

def victory_for(board, sign):
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combination in win_combinations:
        if all(board[row][col] == sign for row, col in combination):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = free_fields[randrange(len(free_fields))]
        board[move[0]][move[1]] = 'X'




board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("Комп'ютер виграв!")
        break
    if victory_for(board, 'O'):
        print("Ви виграли!")
        break
    if not make_list_of_free_fields(board):
        print("Нічия!")
        break

    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("Ви виграли!")
        break

    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("Комп'ютер виграв!")
        break
