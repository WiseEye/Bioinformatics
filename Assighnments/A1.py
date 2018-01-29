# Author: Daniel Heinen
# Assighnment: A1
# Date: 1/29/2018


strand1 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" #string for part 1
strand2 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"#string for part 2
strand3 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"#string for part 3
strand4 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"#string for part 4

# definitions for functions

    #solution one is a function that finds the AT content using the idea 
    #that AT Content = (number of As + number of Ts) / (length of the sequence)
def solutionOne():
    print "Part 1 For Strand: ", strand1
    print "AT content = ", (strand1.count('A') + strand1.count('T'))/ 2
    
    #solution two finds the location of GAATTC and finds the size of
    #the fragment that would be created by cutting using EcoRI restriction enzyme
def solutionTwo():
    print "\n\n\nPart 2 For Strand: ", strand2
    loc = strand2.find('GAATTC') + 1 # account for array starting at 0
    fragOneLength = len(strand2[loc: len(strand2)])
    fragTwoLength = len(strand2) - fragOneLength
    print "The Length of the two fragments are:", fragTwoLength, "and", fragOneLength
    
    #prints the compliment of the given strand of DNA
def solutionThree():
    print "\n\n\nPart 3 For Strand: ", strand3
    #in the next line we replace each nucliatide with its lowercase compliment 
    #a for loop would be better but for the sake of this project we will be fine 
    compliment = strand3.replace('A','t').replace('G','c').replace('T','a').replace('C','g')
    print "compliment = ", compliment.upper()
    
    #prints a strand of DNA printing the extrons in uppercase and the introns in 
    #lowecase. This works by using the locations given to us in the homework
def solutionFour(strand4):
    print "\n\n\nPart 4 For Strand: ", strand4
    strand4 = strand4.lower() #makes all chars to lowercase
    #the next line of code replaces the parts of the string that are said to be
    #extrons with uppercase chars and leaves the intons as lowercase
    print strand4.replace(strand4[0:63], strand4[0:63].upper()).replace(strand4[90:len(strand4)], strand4[90:len(strand4)].upper())

    
    
    
    
    
    
    
    

solutionOne()
solutionTwo()
solutionThree()
solutionFour(strand4) #we pass in strand4 becuase we do not want to use it in a global context





