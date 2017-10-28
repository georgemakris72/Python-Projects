class EggBasketHunt():
    import random
    basket=[]
    egg1=random.randint(1,6)
    egg2=random.randint(1,6)
    egg3=random.randint(1,6)
    egg4=random.randint(1,6)
    egg5=random.randint(1,6)
    egg6=random.randint(1,6)
    bucket=random.randint(1,6)
    basket.append(0)
    print(egg1,egg2,egg3,egg4,egg5,egg6,basket[0])

    class room0(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            movement = input("Possible exits are: N").upper()
            if (movement=='N'):
                room = room10()
                room
            if (movement=='S'):
                if(len(basket)==7):
                    print("You win!!!!")
                else:
                    print("Keep trying... You can't leave without a full basket!")
            else:
                print ("You can't go that way")
                room = room0()
                room

    class room1(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            getItems(1)
            movement = input("Possible exits are: S").upper()
            if (movement=='S'):
                room = room7()
                room
            else:
                print ("You can't go that way")
                room = room1()
                room

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

    class room3(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            getItems(3)
            movement = input("Possible exits are: S").upper()
            if (movement=='S'):
                room = room9()
                room
            else:
                print ("You can't go that way")
                room = room3()
                room

    class room4(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            getItems(4)
            movement = input("Possible exits are: N").upper()
            if (movement=='N'):
                room = room7()
                room
            else:
                print ("You can't go that way")
                room = room4()
                room

    class room5(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            getItems(5)
            movement = input("Possible exits are: N").upper()
            if movement == "N":
                room = room8()
                room
            else:
                print ("You can't go that way")
                room = room5()
                room

    class room6(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            getItems(6)
            movement = input("Possible exits are: N").upper()
            if (movement=='N'):
                room = room9()
                room
            else:
                print ("You can't go that way")
                room = room6()
                room

    class room7(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            movement = input("Possible exits are: N E S").upper()
            if movement == "N":
                room = room1()
                room
            if movement == "S":
                room = room4()
                room
            if movement == "E":
                room9  = room8()
                room
            else:
                print ("You can't go that way")
                room = room7()
                room

    class room8(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
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

    class room9(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self):
            movement = input("Possible exits are: N E S W").upper()
            if (movement=='N'):
                room = room3()
                room
            elif (movement=='S'):
                room = room6()
                room
            elif (movement=='E'):
                room = room10()
                room
            elif (movement=='W'):
                room = room8()
                room
            else:
                print ("You can't go that    way")
                room = room9()
                room

    class room10(EggBasketHunt):
        def __init__(self):
            EggBasketHunt._init_(self)
            movement = input("Possible exits are: S W").upper()
            if movement == "w":
                room = room9()
                room
            if movement == "S":
                room = room0()
                room
            else:
                print ("You can't go that way")
                room = room10()
                room
game = EggBasketHunt()
game
