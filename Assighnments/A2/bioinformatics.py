
def pctOfProtein(sequence, code):
    sequenceUpper = sequence.upper() #sets the sequesnce string to all uppercase letters
    count = 0 # holds a count of letters in our list found in our sequesnce string
    
    for letter in code:#loops through our list checking the count for letters in our sequence string
         count = count + sequenceUpper.count(letter.upper()) 
    
    print (100/len(sequence))*count #prints percents
    
