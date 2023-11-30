from math import sqrt

print("Calculator\n")

def addition():
    print(int(input("Input number one: ")) + int(input("Input number two: ")))

def subtraction():
    print(int(input("Input number one: ")) - int(input("Input number two: ")))

def multiplication():
    print(int(input("Input number one: ")) * int(input("Input number two: ")))

def division():
    print(round(int(input("Input number one: ")) / int(input("Input number two: ")), 3))

def power():
    print(int(input("Input number for exponentation: ")) ** int(input("Input power of number: ")))

def squareRoot():
    print(round(sqrt(int(input("Input number for square root: "))), 3))

def main():
    while True:
        print("Choice operation: +, -, *, /, ^, sqrt or q to exit")
        operator = input("Input operator: ")
        print("=" * 27)

        match operator:
            case "+":
                addition()
            case "-":
                subtraction()
            case "*":
                multiplication()
            case "/":
                division()
            case "^":
                power()
            case "sqrt":
                squareRoot()
            case "q":
                exit()
            case _:
                print("Invalid choice\n")
                continue

main()