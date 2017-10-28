
# coding: utf-8

# In[42]:

def getItems(x):
    getEgg = 'You found an egg! You have placed it in your basket'
    leaveEgg = 'You found an egg! But you do not have a basket to carry it in yet...'
    if basket[0] == x:
        print('You found the basket! It is now in hand.')
        basket[0] = 11
    if egg1 == x:
        if basket[0] == 11:
            print(getEgg)
            egg1 = 11
            basket.append(egg1)
        else:
            print(leaveEgg)
    if egg2 == x:
        if basket[0] == 11:
            print(getEgg)
            egg2 = 11
            basket.append(egg2)
        else:
            print(leaveEgg)
    if egg3 == x:
        if basket[0] == 11:
            print(getEgg)
            egg3 = 11
            basket.append(egg3)
        else:
            print(leaveEgg)
    if egg4 == x:
        if basket[0] == 11:
            print(getEgg)
            egg4 = 11
            basket.append(egg4)
        else:
            print(leaveEgg)
    if egg5 == x:
        if basket[0] == 11:
            print(getEgg)
            egg5 = 11
            basket.append(egg5)
        else:
            print(leaveEgg)
    if egg6 == x:
        if basket[0] == 11:
            print(getEgg)
            egg6 = 11
            basket.append(egg6)
        else:
            print(leaveEgg)

