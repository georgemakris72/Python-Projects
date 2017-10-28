class room2(EggBasketHunt):
    def __init__(self):
        EggBasketHunt._init_(self)
        getItems(2)
        movement = input("Possible exits are: S").upper()
        if movement == "S":
            room = room8()
            room
        else: 
            print ("You can't go that way")
            room = room2()
            room

class room5(EggBasketHunt):
    def __init__(self):
    getItems(5)
    movement = input("Possible exits are: N").upper()
    if movement == "N":
        room = room8()
        room
    else:
        print ("You can't go that way")
        room = room5()
        room

class room8(EggBasketHunt):
    def __init__(self):
    getItems(8)
    movement = input("Possible exits are: N E S W").upper()
    if movement == "N":
        room = room2()
        room
    if movement == "S":
        room = room5()
        room
    if movement == "E":
        room9  = room9()
        room
    if movement == "W":
        room7 = room7()
        room
    else:
        print ("You can't go that way")
        room = room8()
        room
        


