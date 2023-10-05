print(""" 
From celcius to farenheit - (1)
From farenheit to celcius - (2)
""")

userChoice = input("Input your choice: ")
if userChoice != "1" and userChoice != "2":
    print("Invalid choice")
    exit()

degree = int(input("Input degree to convert: "))

if userChoice == "1":
    print("=" * 27)
    print(f"Result: {round(degree * 1.8 + 32)}°F")
else:
    print("=" * 27)
    print(f"Result: {round((degree - 32) / 1.8)}°C")
