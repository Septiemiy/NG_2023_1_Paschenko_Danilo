from math import sqrt

print("Calculator\n")

def addition():
    result = int(input("Input number one: ")) + int(input("Input number two: "))
    return result

def subtraction():
    result = int(input("Input number one: ")) - int(input("Input number two: "))
    return result

def multiplication():
    result = int(input("Input number one: ")) * int(input("Input number two: "))
    return result

def division():
    result = round(int(input("Input number one: ")) / int(input("Input number two: ")), 3)
    return result

def power():
    result = int(input("Input number for exponentation: ")) ** int(input("Input power of number: "))
    return result

def squareRoot():
    result = round(sqrt(int(input("Input number for square root: "))), 3)
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