string = input("Input string: ").lower()

vowels = "aeiou"

print("Result: ", end = "")
for letter in string:
    if letter in vowels:
        print(f"{letter}, ", end = "")