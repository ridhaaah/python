names = ["Sara","Aman","David","Riya","Arav"]
count_a = 0
for name in names:
    count_a += name.lower().count('a')
    print("The letter 'a' occurs",count_a, "times in the list.")
