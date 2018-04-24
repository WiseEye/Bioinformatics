import BIOL420

file = open('data.csv', 'r')

for line in file:#itterates through csv file
    sequenceData = line.split(',') # splits line on ',' into array 
    sequence =  sequenceData[1] #gets sequence
    if(BIOL420.low(sequence)):
        print("This gene is %s and this sequence has a low AT content " % (sequenceData[2]))
        
    elif(BIOL420.med(sequence)):
        print("This gene is %s and this sequence has a medium AT content " % (sequenceData[2]))
        
    elif(BIOL420.high(sequence)):
        print("This gene is %s and this sequence has a high AT content " % (sequenceData[2]))
        