# Problem: https://docs.google.com/document/d/1nivnnq4IlPDeW0sA_d7FHa4NNKOWE8uQSGSwPXALEZw/edit?usp=sharing

valid = False
while not valid:
    # prompt the user for a word
    w = input('Enter a word: ')
    
    if len(w) in range(1, 101):
        # determine and display the distinct letters of the word
        n = len(set(w.lower()))
        print(f'The number of distinct letters appearing in W: {n}')
        
        valid = True
    else:
        print('Enter the word whose length is between 1 and 100 inclusive! \n')
