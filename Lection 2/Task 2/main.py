elementsList = input("Input what you want: ").split(" ")

numberCount = 0

for element in elementsList:
    try:
        int(element)
        numberCount += 1
    except:
        continue

print(f"\nCount of number in list: {numberCount}")