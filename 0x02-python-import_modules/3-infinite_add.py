#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argu = sys.argv
    new_argu = numeric_integers = [int(x) for x in argu if x.isdigit() or (x[0] == '-' and x[1:].isdigit())]
    sum_argu = sum(new_argu)
    print("{}".format(sum_argu))
