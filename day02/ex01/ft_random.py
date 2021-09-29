from random import randrange

def gen_random(n):
    randomList = [randrange(1,401) for i in range(n)]
    return randomList