def pctOfProtein(sequence, code):
    sequenceUpper = sequence.upper()
    count = 0
    
    for letter in code:
         count = count + sequenceUpper.count(letter.upper()) 
    
    print (100/len(sequence))*count #prints percents
    
