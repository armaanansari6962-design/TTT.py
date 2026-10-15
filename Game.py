
board = [" "for i in range(9)]

def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
    
def check_winner(player):
    win_position = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8,],[2,4,6]
    ]
    
    for pos in win_position:
        if all(board[i] == player for i in pos):
            return True
    return False

player = "X"

for turn in range(9):
    show_board()
    print("player",player)
    
    try:
        move = int(input("Enter your position(1-9): ")) - 1 
    except ValueError:
        print("Please enter a number")
        continue
    
    if move < 0 or move > 8 or board[move] != " ":
        print("Enter invalid number")
        continue
    
    board[move] = player
    
    if check_winner(player):
        show_board()
        print("Player",player,"wins!")
        break
    
    player = "O" if player == "X" else "X"
    
else:
    show_board()
    print("Its a Draw!")

