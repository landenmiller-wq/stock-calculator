# Stock Investment Calculator - Version 2
# Calculate investment cost, current value, profit/loss, and return

stock_name = "Apple"
number_of_shares = 10
share_price = 150

# Version 1 calculation: total cost
total_cost = number_of_shares * share_price

# Step 11: New stock price
new_share_price = 175

# Step 12: Current investment value
current_value = new_share_price * number_of_shares

# Step 13: Profit or loss
profit_loss = current_value - total_cost

# Step 14: Percentage return
percentage_return = (profit_loss / total_cost) * 100

# Step 15: Display the results
print("Stock:", stock_name)
print("Number of shares:", number_of_shares)
print("Original price per share: $", share_price)
print("Total investment cost: $", total_cost)
print("New price per share: $", new_share_price)
print("Current investment value: $", current_value)
print("Profit/Loss: $", profit_loss)
print("Percentage return:", round(percentage_return, 2), "%")