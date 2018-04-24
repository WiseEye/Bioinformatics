# Name: Daniel Heinen
# Date: 4/23/2018
# Class: BIOL420

#Function: Get the percentage a codeon makes up of a strand
def pctOfProtein(sequence, code):
    sequenceUpper = sequence.upper() #sets the sequesnce string to all uppercase letters
    count = 0 # holds a count of letters in our list found in our sequesnce string
    for letter in code:#loops through our list checking the count for letters in our sequence string
         count = count + sequenceUpper.count(letter.upper()) 
    print (100/len(sequence))*count #prints percents
    
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

#Function: Translate codins into amino acids from an amino acid lookup table
def translate_dna(sequence):
    #size of condons
    n = 3
    aminoacide=[]
    #splits the string into a list of codons
    sequence=[sequence[i:i+n] for i in range(0, len(sequence), n)]
    #loops through the dictionary gets the matching amino acid and ads it to the a list
    for codon in sequence:
        aminoacide.append(gencode.get(codon))
    #turns our list into a string
    return ''.join(aminoacide)


gencode = {
 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}