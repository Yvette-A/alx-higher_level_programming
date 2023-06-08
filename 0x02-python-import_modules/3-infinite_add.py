#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsCount = len(sys.argv) - 1
    sumOfArgs = 0
    for i in range(argsCount):
        sumOfArgs += int(sys.argv[i + 1])
    print("{}".format(sumOfArgs))
