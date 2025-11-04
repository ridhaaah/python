n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibnoacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibnoacci sequence:")
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
