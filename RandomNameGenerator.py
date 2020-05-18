import random,string
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"

letter1_input=input("enter a letter? enter 'v' for vowels,'c' for consonants,'l' for any letter:")
letter2_input=input("enter a letter? enter 'v' for vowels,'c' for consonants,'l' for any letter:")
letter3_input=input("enter a letter? enter 'v' for vowels,'c' for consonants,'l' for any letter:")
def generator():
    if letter1_input=='v':
        letter1=random.choice(vowels)
    elif letter1_input=='c':
         letter1=random.choice(consonants)
    elif letter1_input=='l':
         letter1=random.choice(string.ascii_lowercase)
    else:
        letter1=letter1_input
        
    if letter2_input=='v':
        letter2=random.choice(vowels)
    elif letter2_input=='c':
         letter2=random.choice(consonants)
    elif letter2_input=='l':
         letter2=random.choice(string.ascii_lowercase)
    else:
        letter2=letter2_input
        
    if letter3_input=='v':
            letter3=random.choice(vowels)
    elif letter3_input=='c':
         letter3=random.choice(consonants)
    elif letter3_input=='l':
         letter3=random.choice(string.ascii_lowercase)
    else:
        letter3=letter3_input
        
    name=letter1+letter2+letter3
    return(name)

for i in range(20):
    print(generator())


        
        
    

    

    
