#!/usr/bin/python3
import sys

from resource import getrusage as res_usage, RUSAGE_SELF
from time import time as t_stamp


def unix_time(function):
    '''Return `real`, `sys`, and `user` elapsed time, like UNIX's command `time`.
    You can calculate the amount of used CPU-time used by your
    function / callable by summing `user` and `sys`. `real is just like
    the wall clock.
    Note that `sys` and `user`'s resolutions are limited by the resolution of the operating system's software clock (check `man 7 time ` for more details).
    '''

    start_time, start_res = t_stamp(), res_usage(RUSAGE_SELF)
    function()
    end_res, end_time = res_usage(RUSAGE_SELF), t_stamp()

    return "\nreal: {}\nuser: {}\nsys: {}\n".format(end_time - start_time,
            end_res.ru_utime - start_res.ru_utime,
            end_res.ru_stime - start_res.ru_stime)


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
