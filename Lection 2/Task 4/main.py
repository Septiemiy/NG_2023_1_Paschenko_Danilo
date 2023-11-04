string = input("Input string: ").lower()
stringList = [(x) for x in string]

lettersDict = {}

vowels = "aeiou"

for letter in stringList:
    if letter in vowels:
        lettersDict[letter] = string.count(letter)
print(f"Result: {lettersDict}")