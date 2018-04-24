import re

file = open('dna.txt', 'r')

data = ''

for line in file:#itterates through txt file
    data+=line
    
#list to hold starting points of splice sites
dnaFragments = []

#start size at 0
dnaFragments.append(0)

#find slpices for enzyme AbcI
for m in re.finditer(r"A.TAAT", line):
    dnaFragments.append(m.start()+3)
    
#find splice site for AbcII 
for m in re.finditer(r"GC(A|G)(A|T)TG", line):
     dnaFragments.append(m.start()+4)

#lastly add the length of string becuase that will be the eind of the prevous spliced strand 
dnaFragments.append(len(data))
dnaFragments.sort()
print dnaFragments
number = 0


for line in dnaFragments:
    number += 1
    if(number >= len(dnaFragments)):
        break
    print("One Strand is %d" % len(data[line:dnaFragments[number]]))

