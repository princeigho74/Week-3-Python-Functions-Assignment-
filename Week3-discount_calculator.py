# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if 20% or higher
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied


# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(price, discount_percent)

    # Print result
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price}")
    else:
        print(f"No discount applied. Final price: {final_price}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
