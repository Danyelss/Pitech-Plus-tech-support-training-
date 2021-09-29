from random import randrange
import time

def main():
    i = 1
    while i <= 10:
        i += 1
        
        value = randrange(10)

        print(value)

        time.sleep(1)

        if value >= 4 and value <= 6:
            raise ValueError

main()




    