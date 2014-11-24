number = 30

userInput = int(raw_input('Please guess a number:'))

if(userInput == 30):
	print 'You got it right man!!'
elif userInput > number:
	print 'The number is a little lower than that!! :('
else:
	print'The number is alittle higher than that'