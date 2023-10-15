number = int(input("Input number: "))

primeNumbersList = []

print("\nNumber:\t|\tIt's dividers:")

for num in range(1, number + 1):
    primeNumberTracker = 0
    print("\n\n" + str(num) + "\t" + "|" + "\t", end = "")
    for divider in range(1, num + 1):
        if num % divider == 0:
            primeNumberTracker += 1
            print(divider, end = " ")
    if primeNumberTracker == 2:
        primeNumbersList.append(num)

print(f"\n\nList of prime numbers: {primeNumbersList}")