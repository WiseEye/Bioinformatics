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