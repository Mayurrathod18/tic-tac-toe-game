#Defining Player 1 and 2 names
Player_1_name = input('Please Enter Player 1's name: ')
Player_2_name = input('Please Enter Player 2's name: ')

print("Player 1 name is: ",Player_1_name)
print("Player 2 name is: ",Player_2_name)

#Printing Tic Tac Toi Board
Board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']]

def TTT_Board(Board):
    for row in Board:
        print(" | ".join(row))

#Defining Player 1 and 2 their values

Player_1 = ''
while Player_1 != 'X' and Player_1 != 'O':
    Player_1 = input("Please selecte between X or O: ").upper()
        
if Player_1 == 'X':
    Player_2 = 'O'

elif Player_1 == 'O':
      Player_2 = 'X'

#Printing PLayer's names
print (f'{Player_1_name} is : ',Player_1)
print (f'{Player_2_name} is : ',Player_2)

def choose_first():
    flip = random.randit(0,1)

    if flip == 0:
        Retu
    

def check_winner(board, symbol):
    # Rows and Columns
    
    for i in range(0,3):
        if all(board[i][j] == symbol for j in range(0,3)) or all(board[j][i] == symbol for j in range(0,3)):
            return True
    # Diagonals
    if all(board[i][i] == symbol for i in range(0,3)) or all(board[i][2 - i] == symbol for i in range(0,3)):
        return True
    return False 
    
def is_draw(board):
    return all(cell != ' ' for Raw_number in board for cell in Raw_number)

# Main game loop
current_player = Player_1
current_name = Player_1_name

while True:
    TTT_Board(Board)
    try:
        Raw_number = int(input(f"{current_name}, enter row number (0-2): "))
        Column_Number = int(input(f"{current_name}, enter column number (0-2): "))

        if Raw_number not in range(0,3) or Column_Number not in range(0,3):
            print("Invalid input. Row and column must be between 0 and 2.")
            continue

        if Board[Raw_number][Column_Number] != ' ':
            print("That cell is already taken. Try again.")
            continue

        Board[Raw_number][Column_Number] = current_player

        # Check for win
        if check_winner(Board, current_player):
            TTT_Board(Board)
            print(f"🎉 {current_name} wins!")
            break

        # Check for draw
        if is_draw(Board):
            TTT_Board(Board)
            print("It's a draw!")
            break
            
        # Switch players
        if current_player == Player_1:
            current_player = Player_2
            current_name = Player_2_name
        else:
            current_player = Player_1
            current_name = Player_1_name
     
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
