import sys

def count_words():
	wordsNumber = 0
	string = sys.stdin.readline()

	index = 0

	while string[index] != '\n' and string[index] != 4:

		while string[index] == ' ' or string[index] == '\t':
			index += 1

		if string[index] != '\n':
			wordsNumber += 1

		while string[index] != '\n' and string[index] != ' ' and string[index] != '\t' and string[index] != 4:
			index += 1

	if wordsNumber == 0:
		raise EOFError('No input provided')
	else:
		return wordsNumber
