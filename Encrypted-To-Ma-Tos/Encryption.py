
# coding: utf-8

# In[9]:

def caesarShift(character):
    List=("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")


	# Wrap the amount
	#if (amount < 0)
	#	return caesarShift(str, amount + 26);

	# Make an output variable
    output = ""
    
	# Go through each character
    for i in range(len(character)):
        
        # Get the character we'll be appending
        c = character[i]
        if (c.isdigit() or c.isalpha()):
            # If it's a letter or number...
            for j in range(len(List)):
                if (c==List[j]):
                
                    # Get its code
                    #	var code = i;
                    
                    # Uppercase letters
                    if ((j >= 0) and (j <= 25)):
                        c = List[(((j - 0 + 7) % 62) + 0)]
                        # Lowercase letters
                    elif ((j >=26 ) and (j <= 51)):
                        c = List[(((j - 26 + 7) % 62) + 26)]
                        # Numbers
                    elif ((j >= 52) and (j <=54)):
                        c = List[(((j - 52 + 7) % 62) + 52)]
                    elif ((j >= 55) and (j <=61)):
                        c = List[(((j - 55 + 7) % 62 -7))]
                        # Append
                    output=output+c
                    c=character[i]
                    
        else:
            output=output+c
        
            # All done!
    return output
    


