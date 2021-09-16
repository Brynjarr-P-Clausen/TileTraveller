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

print(input1(1,1, "n"))