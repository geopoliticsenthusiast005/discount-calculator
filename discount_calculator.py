def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount."""
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Prompt user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    print(f"Final price: {final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
