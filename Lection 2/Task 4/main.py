string = input("Input string: ").lower()
stringList = set([(letter) for letter in string])

print(stringList)

lettersDict = {}

vowels = "aeiou"

for letter in stringList:
    if letter in vowels:
        lettersDict[letter] = string.count(letter)
print(f"Result: {lettersDict}")