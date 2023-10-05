from math import sqrt

inputNumOneMes = "Input first number: "
inputNumTwoMes = "Input second number: "
inputExpNumMes = "Input number for exponentation: "
inputPowerNumMes = "Input power of number: "
inputSqrtNumMes = "Input number for square root: "

print("Calculator\n")

def inputNumber(message):
    return int(input(message))


def main():
    while True:
        print("Choice operation: +, -, *, /, ^, sqrt or q to exit")
        operator = input("Input operator: ")
        print("=" * 27)

        match operator:
            case "+":
                print(f"Result: {inputNumber(inputNumOneMes) + inputNumber(inputNumTwoMes)}\n")
            case "-":
                print(f"Result: {inputNumber(inputNumOneMes) - inputNumber(inputNumTwoMes)}\n")
            case "*":
                print(f"Result: {inputNumber(inputNumOneMes) * inputNumber(inputNumTwoMes)}\n")
            case "/":
                print(f"Result: {round(inputNumber(inputNumOneMes) / inputNumber(inputNumTwoMes), 3)}\n")
            case "^":
                print(f"Result: {inputNumber(inputExpNumMes) ** inputNumber(inputPowerNumMes)}\n")
            case "sqrt":
                print(f"Result: {round(sqrt(inputNumber(inputSqrtNumMes)), 3)}\n")
            case "q":
                exit()
            case _:
                print("Invalid choice\n")

main()