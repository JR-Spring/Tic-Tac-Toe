

#--------Global variables--------

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-",]

#Checks if game is still going
game_still_going = True

#Who won or tie
Winner = None

#Whos turn is it
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])  
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    

def play_game():

   # displayed initial game board 
   display_board()
    #While the game is still going
   while game_still_going:
   
    #Handle a single turn of a arbitrary player
    handle_turn(current_player)

   #Checks if game has ended
    check_if_game_over()
    
    #flips to the other player 
    flip_player()

    #The game has ended.
   if Winner == "X" or Winner == "O":
    print(Winner + " Won.")
   elif Winner == None:
    print("Tie.")


#this function is for whos turn it is
def handle_turn(player):
    
   print(player + "'s turn.")
    #The function input allows an entry onto the game board X or O    
   position = input("Choose a position from 1-9: ")

   valid = False
   while not valid:
    
     while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9",]:
       position = input("Choose a position from 1-9: ")
    
    #The -1 was to offset the elements which are 1-9 and the indexes which are 0-8
     position = int(position) - 1

     if board[position] == "-":
      valid = True 
     else:
      print("Space occupied, choose another spot.")
   
   board[position] = player

   display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set up global variable from the global variable outside of the function
    global Winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()
    
    #Get the winner
    if row_winner:
     Winner = row_winner
    
    elif column_winner:
     Winner = column_winner
    
    elif diagonal_winner:
     Winner = diagonal_winner
    
    else:
        Winner = None
    return
            

def check_rows():
    #Set up global variables
    global game_still_going
    #Check if rows have all the same values either X or O (and it is not equal to - dash in display board)
    row_1 =  board[0] == board[1] == board[2] != "-"
    row_2 =  board[3] == board[4] == board[5] != "-"
    row_3 =  board[6] == board[7] == board[8] != "-"
    #If any row has a match, flag ther there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #Return the winner X or O
    if row_1:
      return board[0]
    if row_2:
      return board[3]
    if row_3:
       return board[6]
    return

def check_columns():
    #Set up global variables
    global game_still_going
    
    #Check if columns have all the same values either X or O (and it is not equal to - dash in display board) 
    columns_1 =  board[0] == board[3] == board[6] != "-"
    columns_2 =  board[1] == board[4] == board[7] != "-"
    columns_3 =  board[2] == board[5] == board[8] != "-"
   
    #If any column has a match, flag ther there is a win
    if columns_1 or columns_2 or columns_3:
        game_still_going = False
    #Return the winner X or O
    if columns_1:
      return board[0]
    if columns_2:
      return board[1]
    if columns_3:
       return board[2]
    
    return

def check_diagonals():
    #Set up global variables
    global game_still_going
    
    #Check if diagonals have all the same values either X or O (and it is not equal to - dash in display board) 
    diagonals_1 =  board[0] == board[4] == board[8] != "-"
    diagonals_2 =  board[6] == board[4] == board[2] != "-"
    
    #This checks to see if there are matches diagonally, if 3 x's or 3 o's diagonally, the game will stop.
    if diagonals_1 or diagonals_2:
        game_still_going = False
    
    #Return the winner X or O
    if diagonals_1:
      return board[0]
    if diagonals_2:
      return board[6]
    return
    
def check_if_tie():
     global game_still_going
     if "-" not in board:
        game_still_going = False
     
     return

def flip_player():
   #global variable needed for this 
   global current_player
   # If current player is x then it will change to o
   if current_player == "X":
       current_player = "O" 
   #If current player is o then it will change it to x
   elif current_player == "O":
       current_player = "X"  
   return


play_game()
  