from math import sqrt

print("Calculator\n")

def main():
    while True:
        print("Choice operation: +, -, *, /, ^, sqrt or q to exit")
        operator = input("Input operator: ")
        print("=" * 27)

        match operator:
            case "+":
                result = int(input("Input first number: ")) + int(input("Input second number: "))
            case "-":
                result = int(input("Input first number: ")) - int(input("Input second number: "))
            case "*":
                result = int(input("Input firs number: ")) * int(input("Input second number: "))
            case "/":
                result = round(int(input("Input first number: ")) / int(input("Input second number: ")), 3)
            case "^":
                result = int(input("Input number for exponentation: ")) ** int(input("Input power of number: "))
            case "sqrt":
                result = round(sqrt(int(input("Input number for square root: "))), 3)
            case "q":
                exit()
            case _:
                print("Invalid choice\n")
                continue
        
        print(f"Result: {result}\n")

main()