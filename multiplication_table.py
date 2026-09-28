num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

for i in range(1, num1 + 1):       # rows
    for x in range(1, num2 + 1):   # columns
        print(f"{i} * {x} = {i * x}")
    print()
