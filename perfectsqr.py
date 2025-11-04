import math

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Four-digit numbers with all even digits and perfect squares:")
for num in range(start, end + 1):
    if 1000 <= num <= 9999:
        root = int(math.sqrt(num))
        if root * root == num:
              digits = str(num)
              if all(int(d) % 2 == 0 for d in digits):
                  print(num)
