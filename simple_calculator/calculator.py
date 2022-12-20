#!/usr/bin/python3

############################## Simple python calculatior #######################################

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(calc, n1, n2):
    return calc(n1, n2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


n1 = float(input("What is the first number? "))

for operation in operations:
    print(operation)

symbol = input("What is the symbol for the operation to be performed ")

calc = operations[symbol]

n2 = float(input("What is the second number? "))


result = calculate(calc, n1, n2)

print(result)
