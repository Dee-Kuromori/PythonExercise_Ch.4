x = input("Enter an number: ")

if "." in x:
    print("X is a float number")
elif "." not in x:
    print(x, "is an integer")