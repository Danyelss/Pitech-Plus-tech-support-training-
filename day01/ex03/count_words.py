def count_words():
	
    string = input()

    string = string.split()

    wordsNumber = len(string)

    if wordsNumber == 0:
        raise EOFError('No input provided')
    else:
        return wordsNumber