# Write a program that calculate and print the following pattern:
#  five friends went for a shopping, calculate the bill, and the tax rate
#  and generate the total amount (tax inclusive) and then divide the total 
#  amount by the friends based on percentage using while loop

def calculate_bill_and_divide():
    # Initial bill amounts for five friends
    bills = [100, 150, 200, 250, 300]  # Example bill amounts
    tax_rate = 0.08  # Example tax rate (8%)

    # Calculate total bill
    total_bill = sum(bills)
    
    # Calculate tax
    tax_amount = total_bill * tax_rate
    
    # Calculate total amount including tax
    total_amount = total_bill + tax_amount
    
    # Friends' contribution percentages (example percentages)
    percentages = [10, 20, 30, 20, 20]
    
    # Convert percentages to proportions
    proportions = [p / 100 for p in percentages]
    
    # Initialize an empty list to store each friend's share
    shares = [0] * len(bills)
    
    # Distribute the total amount using a while loop
    i = 0
    while i < len(proportions):
        shares[i] = total_amount * proportions[i]
        i += 1

    # Print the results
    print(f"Total bill (without tax): ${total_bill:.2f}")
    print(f"Tax amount: ${tax_amount:.2f}")
    print(f"Total amount (tax inclusive): ${total_amount:.2f}")
    print("Amount each friend has to pay:")
    
    for idx, share in enumerate(shares):
        print(f"Friend {idx + 1}: ${share:.2f}")

# Call the function to execute the program
calculate_bill_and_divide()
