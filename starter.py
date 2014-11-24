number = 30
running = True

while(running):
	userInput = int(raw_input('Please guess a number:'))

	if(userInput == 30):
		print 'You got it right man!!'
		running = False
	elif userInput > number:
		print 'The number is a little LOWER than that!! :('
	else:
		print'The number is a little HIGHER than that'
		
else:
	print 'While loop is over'