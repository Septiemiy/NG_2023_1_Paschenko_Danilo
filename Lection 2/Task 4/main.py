string = input("Input string: ")

vowels = "aeiouAEIOU"

vowelsFromStringList = []

for letter in string:
    if letter in vowels:
        vowelsFromStringList.append(letter)

print(f"\nAll vowels from string: {set(vowelsFromStringList)}")