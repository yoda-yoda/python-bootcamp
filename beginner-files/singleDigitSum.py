def getSum(number):
	pass


def getPow(num, exponent):
	return num ** exponent

answer = str(getPow(2, 1000))
digitSum = 0

for digit in answer:
	digitSum += int(digit)

print digitSum
