string = input()

index = 0

firstNumber = 0
secondNumber = 0
firstOk = False
secondOk = False

while (string[index] == ' ' or string[index] == '\t') and index < len(string) - 1:
	index += 1

while string[index] >= '0' and string[index] <= '9' and index < len(string) - 1:
	firstNumber *= 10
	firstNumber += ord(string[index]) - ord('0')
	firstOk = True
	index += 1

while (string[index] == ' ' or string[index] == '\t') and index < len(string) - 1:
	index += 1

while string[index] >= '0' and string[index] <= '9' and index < len(string) - 1:
	secondNumber *= 10
	secondNumber += ord(string[index]) - ord('0')
	secondOk = True
	index += 1

if string[index] >= '0' and string[index] <= '9':
	secondNumber *= 10
	secondNumber += ord(string[index]) - ord('0')
	secondOk = True

while index < len(string) - 1:
	if string[index] != ' ' or string[index] != '\t':
		raise TypeError('Incorrect type')
	else:
		index += 1

if firstOk == False and secondOk == False:
	raise EOFError('No input provided')

if firstOk == False or secondOk == False:
	raise TypeError('Incorrect type')

if firstNumber == secondNumber:
	raise ValueError('invalid interval')

intervalIncrement = firstNumber

while intervalIncrement <= secondNumber:
	print (intervalIncrement, end =" ")
	intervalIncrement += 1

print (" ")
