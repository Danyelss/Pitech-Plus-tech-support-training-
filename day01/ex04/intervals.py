def main():

    string = input()

    if len(string) == 0:
        raise EOFError('No input provided')

    string = string.split()

    if len(string) != 2:
        raise TypeError('Incorrect type')

    for number in string:
        if number.isdigit == False:
            raise TypeError('Incorrect type')

    firstNumber = int(string[0])
    secondNumber = int(string[1])

    if secondNumber < firstNumber:
        raise ValueError('Invalid interval')

    intervalIncrement = firstNumber

    while intervalIncrement <= secondNumber:
        print (intervalIncrement, end =" ")
        intervalIncrement += 1

    print (" ")

if __name__ == "__main__":
   main()
