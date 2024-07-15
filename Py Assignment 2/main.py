# Take two inputs and store them in variables a and b
a = input("Enter the first value (a): ")
b = input("Enter the second value (b): ")

# Print original values
print(f"Original values: a = {a}, b = {b}")

# Switch the values
a, b = b, a

# Print the switched values
print(f"Switched values: a = {a}, b = {b}")
