"""
Convert a string of bits to decimal integer
"""

bstring = raw_input("Enter a string of bits: ")
decimal = 0
exponent = len(bstring) - 1
for digit in bstring:
	decimal = decimal + int(digit) * 2 ** exponent
	exponent = exponent - 1
print "The integer value is", decimal

