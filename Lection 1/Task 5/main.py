from math import sqrt

print("Quadratic equation calculator\n")

inputQuadraticCoefMes = "Input quadratic coefficient: "
inputLinearCoefMes = "Input linear coefficient: "
inputConstantCoefMes = "Input constant coefficient: "

def getNum(message):
    return int(input(message))

def firstRoot(quadraticCoef, linearCoef, discriminant):
    return round((-(linearCoef) + discriminant) / (2 * quadraticCoef), 3)

def secondRoot(quadraticCoef, linearCoef, discriminant):
    return round((-(linearCoef) - discriminant) / (2 * quadraticCoef), 3)

def checkQuadraticCoef(quadraticCoef):
    if quadraticCoef == 0:
        print("\nError: quadratic coefficient mustn`t be zero")
        exit()

def getDiscriminant(quadraticCoef, linearCoef, constantCoef):
    return linearCoef ** 2 - 4 * quadraticCoef * constantCoef

def getNegativeDiscriminant(discriminant, quadraticCoef, linearCoef):
    realUnit = round(-linearCoef / (2 * quadraticCoef), 3)
    imageUnit = round(sqrt(discriminant * (-1)) / (2 * quadraticCoef), 3)
    return f"{realUnit} ± {imageUnit}i"

def main():
    quadraticCoef = getNum(inputQuadraticCoefMes)
    checkQuadraticCoef(quadraticCoef)
    linearCoef = getNum(inputLinearCoefMes)
    constantCoef = getNum(inputConstantCoefMes)

    discriminant = getDiscriminant(quadraticCoef, linearCoef, constantCoef)
    print("=" * 27)

    if discriminant > 0:
        discriminant = sqrt(discriminant)
        print(f"Result: X1 = {firstRoot(quadraticCoef, linearCoef, discriminant)}, X2 = {secondRoot(quadraticCoef, linearCoef, discriminant)}")
    elif discriminant == 0:
        print(f"Result: X1 = {firstRoot(quadraticCoef, linearCoef, discriminant)}")
    else:
        print(f"Result X = {getNegativeDiscriminant(discriminant, quadraticCoef, linearCoef)}")

main()