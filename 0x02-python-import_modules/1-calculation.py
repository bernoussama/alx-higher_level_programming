#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    def printop(a: int, b: int, op):
        operation: str = ""
        match op.__name__:
            case "add":
                operation = "+"
            case "sub":
                operation = "-"
            case "mul":
                operation = "*"
            case "div":
                operation = "/"

        print("{} {} {} = {}".format(a, operation, b, op(a, b)))

    a = 10
    b = 5
    printop(a, b, add)
    printop(a, b, sub)
    printop(a, b, mul)
    printop(a, b, div)
