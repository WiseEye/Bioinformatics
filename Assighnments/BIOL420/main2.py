import BIOL420
# all test code

BIOL420.pctOfProtein("msrslllrfllfllllpplp", ["L"]) # should return 50
BIOL420.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) # should return 5
BIOL420.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) # should return 55
BIOL420.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L']) # should return 70
