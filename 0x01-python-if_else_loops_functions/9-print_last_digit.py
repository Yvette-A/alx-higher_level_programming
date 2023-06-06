#!/usr/bin/python3
def print_last_digit(number):
    lDigit = abs(number) % 10
    print("{}" .format(lDigit), end= "")
    return (lDigit)
