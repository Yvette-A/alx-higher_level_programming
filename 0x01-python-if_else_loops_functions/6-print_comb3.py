#!/usr/bin/python3
for num in range(10):
    for n in range(num + 1, 10):
        if num == 8 and n == 9:
            print("{}{}" .format(num, n))
        else:
            print("{}{}" .format(num, n), end=", ")
