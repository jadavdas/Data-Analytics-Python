# ---------- RECURSIVE FUNCTIONS ----------
# A function that refers to itself is a recursive function

# Calculating factorials is commonly done with a recursive
# function 3! = 3 * 2 * 1
def factorial(num):
    # Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2