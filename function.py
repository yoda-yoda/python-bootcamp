def getSquare(numSquared):
	return numSquared * numSquared
	#end of method()
	
number = int(raw_input('Enter a number to get it\'s square\n'))
print 'The square of',number,'is', getSquare(number)