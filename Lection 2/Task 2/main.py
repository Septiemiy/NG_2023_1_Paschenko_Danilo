elementsList = []

while True:
    element = input("Input what you want(input \"quit\" for exit): ")
    if element == "quit":
        break
    elementsList.append(element)

numberCount = 0

for element in elementsList:
    try:
        int(element)
        numberCount += 1
    except:
        continue

print(f"\nCount of number in list: {numberCount}")