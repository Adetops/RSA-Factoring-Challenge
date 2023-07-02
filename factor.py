#!/usr/bin/python3
import sys

def trial_div(n: int) -> int:
    '''
    Finds the smallest ivisor, if any, of a given number 'n'
    Returns:
        smallest divisor if found
        0 if n is prime
    '''
    # TODO: Create a Clibrary with this function to speed it up.

    while n % 2 == 0:
        return (2)

    f = 3
    while f * f <= n:
        if n % f == 0:
            return f
        else:
            f += 2
    #n is prime
    return (1)


def print_factors():
    with open(sys.argv[1], 'r') as prime:
        line = prime.readline()
        while line != '':
            n = int(line)
            rep = trial_div(n)
            print("{}={}*{}".format(n, n//rep, rep))
            line = prime.readline()
        prime.close()
