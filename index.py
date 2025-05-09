def calculate_discount(price, discount_percent):
    # To check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # To calculate the final price after applying the discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # This will return the original price if the discount is less than 20%
        return price

# Prompt the user to enter the original price and the discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
print(f"The final price is: ${final_price:.2f}")
