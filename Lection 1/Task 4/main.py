from math import sqrt

print("Calculator\n")

def inputNumberOne():
    return int(input("Input number one: "))

def inputNumberTwo():
    return int(input("Input number two: "))

def inputNumberExponentation():
    return int(input("Input number for exponentation: "))

def inputNumberPower():
    return int(input("Input power of number: "))

def inputNumberSquareRoot():
    return int(input("Input number for square root: "))

def addition():
    result = inputNumberOne() + inputNumberTwo()
    return result

def subtraction():
    result = inputNumberOne() - inputNumberTwo()
    return result

def multiplication():
    result = inputNumberOne() * inputNumberTwo()
    return result

def division():
    result = round(inputNumberOne() / inputNumberTwo(), 3)
    return result

def power():
    result = inputNumberExponentation() ** inputNumberPower()
    return result

def squareRoot():
    result = round(sqrt(inputNumberSquareRoot()), 3)
    return result

def outputResult(result):
    print(f"Result: {result}")

def main():
    while True:
        print("Choice operation: +, -, *, /, ^, sqrt or q to exit")
        operator = input("Input operator: ")
        print("=" * 27)

        match operator:
            case "+":
                outputResult(addition())
            case "-":
                outputResult(subtraction())
            case "*":
                outputResult(multiplication())
            case "/":
                outputResult(division())
            case "^":
                outputResult(power())
            case "sqrt":
                outputResult(squareRoot())
            case "q":
                exit()
            case _:
                print("Invalid choice\n")
                continue

main()