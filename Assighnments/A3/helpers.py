#Finds AT content in a sequence/string
def content(strand):
    cleanedStrand = strand.upper()
    return ((float(cleanedStrand.count('A')) + float(cleanedStrand.count('T'))  )/ len(cleanedStrand))
    
#takes a sequence and returns True if the sequence has a high AT Content.
def high(highATSequence):
    if content(highATSequence) > 0.65:
        return True
    else:
        return False
    
#takes a sequence and returns True if the sequence has a medium, AT Content.
def med(mediumATContent):
    if 0.65 > content(mediumATContent) > 0.45  :
        return True
    else:
        return False
    
#takes a sequence and returns True if the sequence has a low AT Content
def low(lowATContent):
    if content(lowATContent) < 0.45:
        return True
    else:
        return False
    