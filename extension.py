filename = input("Enter the file name: ")
parts = filename.split(".")
if len(parts) > 1:
    print("The file extension is:", parts[-1])
else:
    print("No extension found.")
