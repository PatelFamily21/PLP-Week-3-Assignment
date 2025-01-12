def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying the discount if it's 20% or higher.
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount, or the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Prompting the user for input and using the function
def main():
    try:
        # Get the original price from the user
        original_price = float(input("Enter the original price of the item: "))
        # Get the discount percentage from the user
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Print the result
        if discount_percentage >= 20:
            print(f"The final price after applying the discount is: {final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: {original_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()
