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


valid_direction = 0
x = 1
y = 1   


def main():
    # 1. tell user where he can go
    # while x != 3 and y != 1: 
    while x != 3 and y != 1:
        where_you_can_travel(x, y)
    
    # 2. ask user where he wants to go
        input1(x, y)
    # 3. verify input is valid
    # 4a. if valid: move
    # 4b. else: punish user gg go agane
    #else:
    #    print("Victory!")
    # 5. check if destination reached while not tile 7
    
        pass  

def where_you_can_travel(x, y):
    if x == 1 and y == 1:
        print("You can travel: (N)orth. ")
        valid_direction = "n".casefold()
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        valid_direction = "n".casefold(), "e".casefold(), "s".casefold()
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
        valid_direction =  "e".casefold(), "s".casefold()
    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
        valid_direction = "n".casefold()
    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
        valid_direction = "w".casefold(), "s".casefold()        
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
        valid_direction = "w".casefold(), "e".casefold(), 
    elif x == 3 and y == 1:
        print("Victory!")
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
        valid_direction = "n".casefold(),  "s".casefold()
    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.") 
        valid_direction = "w".casefold(), "s".casefold()
    return(valid_direction)

def input1(x, y, path):
    way = input("Direction: ".casefold())
    if way in path:
        if way == "n":
            y += 1
        elif way == "s":
            y =- 1
        elif way == "e":
            x += 1
        elif way == "w":
            x -= 1
    else:
        print("Invalid Direction.")

    return x, y

main()

# print(where_you_can_travel(x, y))
# print(input1(1,1, "n"))

while True:
    where_you_can_travel(x, y)
    
    # 2. ask user where he wants to go
    input1(x, y, where_you_can_travel)
    # 3. verify input is valid
    # 4a. if valid: move
    # 4b. else: punish user gg go agane
