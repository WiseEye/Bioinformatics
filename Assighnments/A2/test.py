import bioinformatics
# all test code

bioinformatics.pctOfProtein("msrslllrfllfllllpplp", ["L"]) # should return 50
bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) # should return 5
bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) # should return 55
bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L']) # should return 70
