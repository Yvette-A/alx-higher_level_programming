#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    assesmentFile = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            assesmentFile.append(True)
        else:
            assesmentFile.append(False)
    return (assesmentFile)
