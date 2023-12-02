#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    calc_argument = argv
    length_argument = len(calc_argument) - 1
    if length_argument == 0:
        print("Usage: {} <a> <operator> <b>".format(calc_argument[0]))
        exit(1)
    ops = {'+':add, '-':sub, '*':mul, '/':div}
    if calc_argument[2] in ops:
        num1 = int(calc_argument[1])
        num2 = int(calc_argument[3])
        op = ops[calc_argument[2]]
        result = op(num1, num2)
        print("{:d} {:s} {:d} = {:d}".format(num1, calc_argument[2], num2, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
