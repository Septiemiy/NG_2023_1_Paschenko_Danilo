file = input("Input file name in order to count all symbols from it: ")

allSymbols = {}

with open(file, "r") as f:
    text = f.read()
    for element in text:
        allSymbols[element] = text.count(element)

print(f"\nCounted all symbols from your file: {allSymbols}")