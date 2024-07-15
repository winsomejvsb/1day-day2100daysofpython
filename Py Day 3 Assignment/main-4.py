#write a program that converts a list to a set when the user types a value,
# it checks if the value already exists in the list, prints a message that 
# the value already exist and removes the duplicate, then prints the list 
# as a set and prompts the user to input again.


def main():
    user_list = []

    while True:
        user_input = input("Enter a value (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        if user_input in user_list:
            print(f"The value '{user_input}' already exists in the list. Removing duplicate...")
            user_list.remove(user_input)
        else:
            user_list.append(user_input)

        user_set = set(user_list)
        print(f"The current set is: {user_set}")

if __name__ == "__main__":
    main()



# This program includes the following steps:
# Initializes an empty list user_list.
# Enters an infinite loop to continuously prompt the user for input.
# If the user types "exit", the loop breaks and the program ends.
# Checks if the input value is already in the list.
# If the value is in the list, it prints a message and removes the duplicate.
# If the value is not in the list, it adds the value to the list.
# Converts the list to a set to remove duplicates and prints the set.
# The loop continues, allowing the user to input more values.
# You can run this program, and it will keep prompting for user input until "exit" is typed. The list will be converted to a set and printed after each input.






