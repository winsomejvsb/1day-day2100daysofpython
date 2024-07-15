 #write a program that converts a string to an integer and checks if the integer is an even number.

def string_to_int_and_check_even(input_string):
    try:
        # Convert the string to an integer
        number = int(input_string)
        
        # Check if the number is even
        if number % 2 == 0:
            return f"The number {number} is even."
        else:
            return f"The number {number} is odd."
    except ValueError:
        return "The input is not a valid integer."

# Example usage
input_string = "43"
result = string_to_int_and_check_even(input_string)
print(result)


# This program includes the following steps:

# Attempts to convert the input string to an integer.
# If the conversion is successful, it checks whether the integer is even or odd.
# If the input string is not a valid integer, it handles the exception and returns an appropriate message.
# You can test this program with different input strings by changing the value of input_string.

