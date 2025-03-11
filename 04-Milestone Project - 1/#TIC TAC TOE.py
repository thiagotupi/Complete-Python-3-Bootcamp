#TIC TAC TOE

#WELCOME MESSAGE
def welcome():
    board_list = [" "," "," "," "," "," "," "," "," "]
    print("Welcome to TIC TAC TOE!")
    print(" ",board_list[6],"|",board_list[7],"|",board_list[8])
    print("-------------")
    print(" ",board_list[3],"|",board_list[4],"|",board_list[5])
    print("-------------")
    print(" ",board_list[0],"|",board_list[1],"|",board_list[2])
    
#DISPLAY INITIAL BOARD
def board():
    pass

#GET POSITION/REPLACE/DISPLAY BOARD
def replace_position1(board_list):
    loopzaum = False
    while loopzaum == False:
        position = input("What position do you want to mark? ")
        try:
            if position.lower == ("stop"):
                return ("Game canceled!")
            position = int(position)
            if position not in range(9):
                raise ValueError("Invalid position. Please enter a number between 0 and 8.")
            if board_list[position] != " ":
                raise ValueError("Position already taken. Try another one.")
            board_list[position] = "X"
            print(" ",board_list[6],"|",board_list[7],"|",board_list[8])
            print("-------------")
            print(" ",board_list[3],"|",board_list[4],"|",board_list[5])
            print("-------------")
            print(" ",board_list[0],"|",board_list[1],"|",board_list[2])
            if (board_list[6] == "X" and board_list[7] == "X" and board_list[8] == "X") or \
               (board_list[6] == "X" and board_list[3] == "X" and board_list[0] == "X") or \
               (board_list[6] == "X" and board_list[4] == "X" and board_list[2] == "X") or \
               (board_list[3] == "X" and board_list[4] == "X" and board_list[5] == "X"):
                loopzaum = True
                return "X VICTORY!!!"                      
            position = (input("What position do you want to mark? "))
            if position == ("stop"):
                return ("Game canceled!")
            position = int(position)
            if position not in range(9):
                raise ValueError("Invalid position. Please enter a number between 0 and 8.")
            if board_list[position] != " ":
                raise ValueError("Position already taken. Try another one.")
            board_list[position] = "O"
            print(" ",board_list[6],"|",board_list[7],"|",board_list[8])
            print("-------------")
            print(" ",board_list[3],"|",board_list[4],"|",board_list[5])
            print("-------------")
            print(" ",board_list[0],"|",board_list[1],"|",board_list[2])
        except ValueError as e:
            print(e)

#LOOP - VICTORY
def victory():
    pass

def game_main():
    board_list = [" "," "," "," "," "," "," "," "," "]
    welcome()
    loopzaum = False
    replace_position1(board_list)
    while True:
        result = replace_position1(board_list)
        if result:
            print(result)
            break
        
    print("GAME OVER")


