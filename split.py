ints = input("Enter a line of list of integers seprated by spaces")
parts = ints.split()
n = []
for p in parts:
    n.append(int(p))

print("Before modifying :")
print(n)

result = []
for num in n:
    if num > 100:
        result.append("over")
    else:
        result.append(num)
print("\n Modified List :")
print(result)
