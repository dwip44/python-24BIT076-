prices = {"apple": 50, "banana": 20, "milk": 30}
quantities = {"apple": 2, "banana": 5, "milk": 1}

total_bill = sum(prices[item] * quantities[item] for item in prices if item in quantities)

print("Total Bill:", total_bill)
