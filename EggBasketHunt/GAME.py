class EggBasketHunt():
    def __init__(self):
        import random
        import sys
        basket=[]
        self.egg1=random.randint(1,6)
        self.egg2=random.randint(1,6)
        self.egg3=random.randint(1,6)
        self.egg4=random.randint(1,6)
        self.egg5=random.randint(1,6)
        self.egg6=random.randint(1,6)
        basketRandom=random.randint(1,6)
        basket.append(basketRandom)
        # print(egg1,egg2,egg3,egg4,egg5,egg6,basket[0])

        def getItems(x):
            getEgg = 'You found an egg! You have placed it in your basket'
            leaveEgg = 'You found an egg! But you do not have a basket to carry it in yet...'
            if basket[0] == x:
                print('You found the basket! It is now in hand.')
                basket[0] = 11
            if self.egg1 == x:
                if basket[0] == 11:
                    print(getEgg)
                    self.egg1 = 11
                    basket.append(self.egg1)
                else:
                    print(leaveEgg)
            if self.egg2 == x:
                if basket[0] == 11:
                    print(getEgg)
                    self.egg2 = 11
                    basket.append(self.egg2)
                else:
                    print(leaveEgg)
            if self.egg3 == x:
                if basket[0] == 11:
                    print(getEgg)
                    self.egg3 = 11
                    basket.append(self.egg3)
                else:
                    print(leaveEgg)
            if self.egg4 == x:
                if basket[0] == 11:
                    print(getEgg)
                    self.egg4 = 11
                    basket.append(self.egg4)
                else:
                    print(leaveEgg)
            if self.egg5 == x:
                if basket[0] == 11:
                    print(getEgg)
                    self.egg5 = 11
                    basket.append(self.egg5)
                else:
                    print(leaveEgg)
            if self.egg6 == x:
                if basket[0] == 11:
                    print(getEgg)
                    self.egg6 = 11
                    basket.append(self.egg6)
                else:
                    print(leaveEgg)

        def room0(EggBasketHunt):
            movement = input("Possible exits are: N and S to LEAVE").upper()
            if (movement=='N'):
                room = room10(EggBasketHunt)
                room()
            if (movement=='S'):
                if(len(basket)==7):
                    print("You win!!!!")
                    sys.exit()
                else:
                    print("Keep trying... You can't leave without a full basket!")
                    room = room0(EggBasketHunt)
                    room()
            else:
                print ("You can't go that way")
                room = room0(EggBasketHunt)
                room()

        def room1(EggBasketHunt):
            getItems(1)
            movement = input("Possible exits are: S").upper()
            if (movement=='S'):
                room = room7(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room1(EggBasketHunt)
                room()

        def room2(EggBasketHunt):
            getItems(2)
            movement = input("Possible exits are: S").upper()
            if movement == "S":
                room = room8(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room2(EggBasketHunt)
                room()

        def room3(EggBasketHunt):
            getItems(3)
            movement = input("Possible exits are: S").upper()
            if (movement=='S'):
                room = room9(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room3(EggBasketHunt)
                room()

        def room4(EggBasketHunt):
            getItems(4)
            movement = input("Possible exits are: N").upper()
            if (movement=='N'):
                room = room7(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room4(EggBasketHunt)
                room()

        def room5(EggBasketHunt):
            getItems(5)
            movement = input("Possible exits are: N").upper()
            if movement == "N":
                room = room8(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room5(EggBasketHunt)
                room()

        def room6(EggBasketHunt):
            getItems(6)
            movement = input("Possible exits are: N").upper()
            if (movement=='N'):
                room = room9(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room6(EggBasketHunt)
                room()

        def room7(EggBasketHunt):
            movement = input("Possible exits are: N E S").upper()
            if movement == "N":
                room = room1(EggBasketHunt)
                room()
            if movement == "S":
                room = room4(EggBasketHunt)
                room()
            if movement == "E":
                room9  = room8(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room7(EggBasketHunt)
                room()

        def room8(EggBasketHunt):
            movement = input("Possible exits are: N E S W").upper()
            if movement == "N":
                room = room2(EggBasketHunt)
                room()
            if movement == "S":
                room = room5(EggBasketHunt)
                room()
            if movement == "E":
                room  = room9(EggBasketHunt)
                room()
            if movement == "W":
                room = room7(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room8(EggBasketHunt)
                room()

        def room9(EggBasketHunt):
            movement = input("Possible exits are: N E S W").upper()
            if (movement=='N'):
                room = room3(EggBasketHunt)
                room()
            elif (movement=='S'):
                room = room6(EggBasketHunt)
                room()
            elif (movement=='E'):
                room = room10(EggBasketHunt)
                room()
            elif (movement=='W'):
                room = room8(EggBasketHunt)
                room()
            else:
                print ("You can't go that    way")
                room = room9(EggBasketHunt)
                room()

        def room10(EggBasketHunt):
            movement = input("Possible exits are: S W").upper()
            if movement == "W":
                room = room9(EggBasketHunt)
                room()
            if movement == "S":
                room = room0(EggBasketHunt)
                room()
            else:
                print ("You can't go that way")
                room = room10(EggBasketHunt)
                room()

        room0(EggBasketHunt)


EggBasketHunt.__call__()
