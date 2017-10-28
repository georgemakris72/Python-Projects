
# coding: utf-8

# In[ ]:

class room3(EggBasketHunt):
    def __init__(self):
        EggBasketHunt._init_(self)
        getItems(3)
        if (movement=='S'):
            Room9()
        else:
            print("you must pick a different direction")
            
            
class room6(EggBasketHunt):
    def __init__(self):
        EggBasketHunt._init_(self)
        getItems(6)
        if (movement=='N'):
            Room9()
        else:
            print("you must pick a different direction")
            
class room9(EggBasketHunt):
    def __init__(self):
        EggBasketHunt._init_(self):
        if (movement=='N'):
            Room3()
        elif (movement=='S'):
            Room6()
        elif (movement=='E'):
            Room10()
        elif (movement=='S'):
            Room8()
        else:
            print("you must pick a different direction")
            
        

