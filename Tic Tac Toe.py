import random


board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')

def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
 
    for col in range(3):
        if all(board[i][col] == player for i in range(3)):
            return True
    
   
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
        
    return False

def make_move(player):
    while True:
        row = int(input('Enter the row number (1 to 3) / Введите номер строки (от 1 до 3): ')) - 1
        col = int(input('Enter the column number (1 to 3) / Введите номер столбца (от 1 до 3): ')) - 1
        
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player
            break
        else:
            print('Invalid move. Try again. / Некорректный ход. Попробуйте снова.')

def bot_move():
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))
   
    if (1, 1) in empty_cells:
        row, col = 1, 1
    elif (0, 0) in empty_cells:
        row, col = 0, 0
    elif (0, 2) in empty_cells:
        row, col = 0, 2
    elif (2, 0) in empty_cells:
        row, col = 2, 0
    elif (2, 2) in empty_cells:
        row, col = 2, 2
    else:
        row, col = random.choice(empty_cells)
    
    board[row][col] = 'O'

def play_with_bot():
    current_player = 'X'
    
    while True:
        print_board()
        
        if current_player == 'X':
            print(f"Player {current_player}'s turn / Ходит игрок {current_player}")
            make_move(current_player)
        else:
            print("Bot's turn / Ходит бот")
            bot_move()
        
        if check_winner(current_player):
            print_board()
            if current_player == 'X':
                print('You have won! / Вы победили!')
            else:
                print('The bot has won! / Бот победил!')
            break
        
        if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
            print_board()
            print("It's a tie! / Ничья!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

def play_with_friend():
    player1 = 'X'
    player2 = 'O'
    current_player = player1
    
    while True:
        print_board()
        
        print(f"Player {current_player}'s turn / Ходит игрок {current_player}")
        make_move(current_player)
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} has won! / Игрок {current_player} победил!")
            break
        
        if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
            print_board()
            print("It's a tie! / Ничья!")
            break
        
        current_player = player2 if current_player == player1 else player1

def choose_game():
    while True:
        print('Select game type / Выберите тип игры:')
        print('1. Play against the bot / Игра с ботом')
        print('2. Play against a friend / Игра с другом')
        game_type = int(input('Enter the number of the chosen option / Введите номер выбранного варианта: '))
        
        if game_type == 1:
            play_with_bot()
        elif game_type == 2:
            play_with_friend()
        
        play_again = input('Do you want to play another round? (yes/no) / Хотите сыграть ещё раз? (да/нет) ')
        if play_again.lower() != 'yes' and play_again.lower()!= 'да':
            break
            
choose_game()
