#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nOfArgs = len(sys.argv) - 1
    if nOfArgs == 0:
        print("0 arguments.")
    elif nOfArgs == 1:
        print("1 argument:")
    else:
        print("{} arguments:" .format(nOfArgs))
    for i in range(nOfArgs):
        print("{}: {}" .format(i + 1, sys.argv[i + 1]))
