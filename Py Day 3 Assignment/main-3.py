# write a program that convert a string to a boolean value by checking
#  against a set of string that represent true values.

def string_to_boolean(input_string):
    # Define a set of strings that represent true values
    true_values = {"true", "yes", "1", "y", "t"}

    # Convert the input string to lowercase to ensure case-insensitive comparison
    input_string_lower = input_string.lower()

    # Check if the input string is in the set of true values
    if input_string_lower in true_values:
        return True
    else:
        return False

# Example usage
input_string = "Yes"
result = string_to_boolean(input_string)
print(f"The boolean value of '{input_string}' is {result}.")



# This program includes the following steps:
# Defines a set of strings that are considered as true values.
# Converts the input string to lowercase to ensure case-insensitive comparison.
# Checks if the lowercase input string is in the set of true values.
# Returns True if the input string is in the set of true values, otherwise returns False.
# You can test this program with different input strings by changing the value of input_string.