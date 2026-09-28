num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

print("   " + "".join(f"{x:>4}" for x in range(1, num2 + 1)))

for i in range(1, num1 + 1):
    row = "".join(f"{i * x:>4}" for x in range(1, num2 + 1))
    print(f"{i:<3}{row}")
