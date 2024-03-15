#!/usr/bin/python3
if __name__=="__main__":
    from sys import argv

    ves = len(argv) - 1

    if ves < 1:
        print("{} arguments.".format(ves))
    elif ves== 1:
        print("{} argument:".format(ves))
    else:
        print("{} arguments:".format(ves))
    for i in range(ves):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
