"""
Lets do a basic math problem
"""

# TODO: perform all of the following mathematical operations and print the results in between

# TODO: set a constant tax rate of 20%

# TODO: ask a user what their revenue was for the quarter

# TODO: deduct the tax rate from the revenue and print the profit as well as the tax amount

# TODO: split that profit evenly amongst 7 share holders

# TODO: print out what each shareholder will receive from the profit
add, subtract, multi, divid, exp, remain = 2 + 2, 4 - 3, 4 * 5, 6 / 3, 4 ** 2, 120 % 5
print(add, subtract, multi, divid, exp, remain)
tax_rate= .2
revenue_quarter = int(input("What was your revenue last quarter?: "))
tax = revenue_quarter * tax_rate
profit = revenue_quarter - (revenue_quarter * tax_rate)
print("We made this much last quarter", str(profit), "and we paid this much in taxes", str(tax))
shareholders = profit / 7
print("We made this much last quarter", str(profit), "and we paid this much in taxes", str(tax), ", and each shareholder made", str(round(shareholders, 2)), ".")
# !! extra credit: print the remainder of the total profit divided by 6
