def count_words():
	wordsNumber = 0
	string = input()

	index = 0

	while index < len(string) - 1 and string[index] != 4:

		while ( string[index] == ' ' or string[index] == '\t') and index < len(string) - 1:
			index += 1

		if string[index] != ' ' and string[index] != '\t':
			wordsNumber += 1

		while ( string[index] != ' ' and string[index] != '\t') and index < len(string) - 1:
			index += 1

	if wordsNumber == 0:
		raise EOFError('No input provided')
	else:
		return wordsNumber
