elementsList = input("Input what you want: ").split(" ")
elementsListSet = set(elementsList)

numberDict = {}

for elem in elementsListSet:
    try:
        int(elem)
        numberDict[elem] = elementsList.count(elem)
    except:
        continue

print(f"Count of numbers in list: {numberDict}")