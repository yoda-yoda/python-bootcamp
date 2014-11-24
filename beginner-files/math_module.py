import math

def getSquare(x):
	return x*x;
	#endOfFn

def raiseNumber(x, y):
	if y == 1:
		return x
	elif y == 0:
		return 1
	else:
		return math.pow(x,y)

number = int(raw_input('Enter a number'))
raisedNumber = int(raw_input('Raising number'))

print "The number %d raised to %d is, %d " % (number, raisedNumber, raiseNumber(number, raisedNumber)) 
	#endOfFn