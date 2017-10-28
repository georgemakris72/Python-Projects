
# coding: utf-8

# In[ ]:

# x="hippopataumus"
# print (x.count("p"))
# print(len(x))
# for k in range(3):
#     x+=str("z")
# print(x)
# s= list(x)
# s[4]="w"
# s="".join(s)
# print(s)

    
from random import randint
def hangman():
    x=["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
    word=randint(0,5)
    r=list(x[word])
    total=0
    z=[]
    
    for i in range(len(r)):
        z.append("^")
    
    for j in range(100):
        guess = input("Please guess a letter: ").lower()
        h=0
        if not guess.isalpha():
            print("You can only enter in a letter.")
        else:
            if(guess in z):
                print("This letter is already in puzzle.")
            else:  
                for k in range(len(r)):
                    if (r[k]==guess):
                        z[k]=guess
                        h=h+1
                        multiple=z.count(r[k])
                        if(z==r):
                            print("You have guessed correctly and found {} new letter(s)".format(multiple))
                            print("YOU HAVE WON THE GAME!!!")
                            return
                if(h>=1):        
                    print("You have guessed correctly and found {} new letter(s)".format(multiple))
            if (h<1):
                if(guess not in z):
                    print("You have guessed incorrectly.")
                    total=total+1
                    if(total==1):
                        print("The post has been added.")
                    elif (total==2):
                        print("The head has been added.")
                    elif (total==3):
                        print("The body has been added.")
                    elif (total==4):
                        print ("One arm has been added.")
                    elif (total==5):
                        print ("Another arm has been added.")
                    elif (total==6):
                        print ("One leg has been added.")
                    elif (total==7):
                        print ("Another leg has been added.")
                    elif (total == 8):
                        print ("The noose has been added.  YOU ARE DEAD!!!")
                        return
                 
        
                
                
        
hangman()          




# In[ ]:




# In[ ]:



