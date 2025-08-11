Python Functions Assignment solution:

# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(price, discount_percent)

    # Display result
    if discount_percent >= 20:
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")

How it works:

1. calculate_discount()

Takes price and discount_percent as inputs.

If the discount is 20% or more, it applies it.

Otherwise, returns the original price.

2. User Input

Prompts for original price and discount percentage.

3. Output

Prints final price with discount if applied.

Prints original price if discount < 20%.
