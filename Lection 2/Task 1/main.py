elementsList = []
element = ""

while True:
    element = input("Input what you want (input \"quit\" for exit): ")
    if element == "quit":
        break
    elementsList.append(element)

print(f"List with unique elements: {set(elementsList)}")