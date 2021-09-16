#Make functions:
    #Start the game
        #Place user in first box (1,1)
    #Where you can travel
        #Check directions to travel and print available paths
    #Input
        #Take input from user
    #Confirm if valid
        #Check if input matches one of available paths
    #Victory condition
        #User has reached last box, (3,1) print victory and stop running

#Algorithm
    #Start game 1.1
        #User options: What the user can do, which movements the user can choose from and make a decision. 
        #Input: The program takes in the input from the user (n, e, w or s) and checks if the input matches the available paths the user is given beforehand to confirm it. 
        #Repeat: The program puts the user in the new location, after the program has checked if the input matches the available paths and repeats the command until the final destination is reached.
    #Victory 3.1

tile1 = 1.1 
tile2 = 1.2
tile3 = 1.3
tile4 = 2.1
tile5 = 2.2
tile6 = 2.3
tile7 = 3.1
tile8 = 3.2
tile9 = 3.3
valid_direction = 0


def main():
    # 1. tell user where he can go
    # 2. ask user where he wants to go
    # 3. verify input is valid
    # 4a. if valid: move
    # 4b. else: punsih user go agane
    # 5. check if destination reached while not tile 7
    location = tile1
    x, y = 1, 1
    y += 1 #norður
    y -= 1 #suður
    x += 1 #austur
    x -= 1 #vestur
    pass


def location(l):
    
    return l

def where_you_can_travel():
    if location == tile1:
        print("You can travel: (N)orth. ")
        valid_direction = "n".casefold()
    elif location == tile2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        valid_direction = "n".casefold(), "e".casefold(), "s".casefold()
    elif location == tile3:
        print("You can travel: (E)ast or (S)outh.")
        valid_direction =  "e".casefold(), "s".casefold()
    elif location == tile4:
        print("You can travel: (N)orth.")
        valid_direction = "n".casefold()
    elif location == tile5:
        print("You can travel: (S)outh or (W)est.")
        valid_direction = "w".casefold(), "s".casefold()        
    elif location == tile6:
        print("You can travel: (E)ast or (W)est.")
        valid_direction = "w".casefold(), "e".casefold(), 
    elif location == tile7:
        print("Victory!")
    elif location == tile8:
        print("You can travel: (N)orth or (S)outh.")
        valid_direction = "n".casefold(),  "s".casefold()
    elif location == tile9:
        print("You can travel: (S)outh or (W)est.") 
        valid_direction = "w".casefold(), "s".casefold()
    return(valid_direction)

def input1():
    input("Direction: ")
    return(input1)

def confirm_if_valid():
    if input1 == valid_direction:
        #go to next location
        print()
    else:
        print("Invalid Direction")


main()