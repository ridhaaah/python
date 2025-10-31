list1 = list(map(int, input("Enter first list of integers(seprated by space):").split()))
list2 = list(map(int, input("Enter second list of integers(seprated by space):").split()))

same_length = len(list1) == sum(list2)
same_sum = sum(list1) == sum(list2)
common_values = set(list1) & set(list2)
print("\nResults:")
print("(a) Lists are of same length:", same_length)
print("(b) Lists have same sum:", same_sum)
print("(c) Common values:", common_values if common_values else "No common values")
             
             

             
