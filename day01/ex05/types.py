def create_types():
	try:
		file = open('demo.txt', 'r')

		string = file.read()
		if len(string) == 0:
			raise EOFError('Invalid input')

		string = string.strip()

		listString = string.split(',')

		for numberFromString in listString:
			if numberFromString.isdigit() == False:
				raise TypeError('Incorect input')

		for i in range(0, len(listString)):
			listString[i] = int(listString[i])

		tupleString = tuple(map(int, string.split(',')))
		dictionary = {i: listString [i] for i in range(0, len(listString ), 1)}

		return listString, tupleString, dictionary

	except FileNotFoundError as e:
		e.strerror = 'Invalid input'
		raise e

