import helpers

file = open('data.csv', 'r')

for line in file:#itterates through csv file
    sequenceData = line.split(',') # splits line on ',' into array 
    sequence =  sequenceData[1] #gets sequence
    if(helpers.low(sequence)):
        print("This gene is %s and this sequence has a low AT content " % (sequenceData[2]))
        
    elif(helpers.med(sequence)):
        print("This gene is %s and this sequence has a medium AT content " % (sequenceData[2]))
        
    elif(helpers.high(sequence)):
        print("This gene is %s and this sequence has a high AT content " % (sequenceData[2]))
        