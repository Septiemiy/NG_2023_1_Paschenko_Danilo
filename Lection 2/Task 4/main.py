string = input("Input string: ")

vowels = "aeiouAEIOU"

print("Result: ", end = "")
for letter in string:
    if letter in vowels:
        print(f"{letter}, ", end = "")