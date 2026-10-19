# WEEK 1 - Introduction to Python Programming

# ---------- Hands-on 1: temperature converter ----------
celsius = 25                                  # a variable (int) holding a temperature in Celsius
fahrenheit = celsius * 9 / 5 + 32             # operators: convert C to F using the standard formula
print("Temperature:", celsius, "C =", fahrenheit, "F")   # output: show the result

# ---------- Hands-on 2: calculator ----------
def calculator(a, b, op):                     # a function so the calculator can be reused
    if op == "+":                             # conditional: choose the operation
        return a + b                          # addition
    elif op == "-":
        return a - b                          # subtraction
    elif op == "*":
        return a * b                          # multiplication
    elif op == "/":
        if b == 0:                            # nested if: avoid dividing by zero
            return "Cannot divide by zero"    # friendly message instead of a crash
        return a / b                          # division
    else:
        return "Unknown operator"             # any other symbol is invalid

print("8 + 2 =", calculator(8, 2, "+"))       # test each operator with sample numbers
print("8 / 0 =", calculator(8, 0, "/"))       # test the error case too

# ---------- Client project: average temperature ----------
temps = [28.5, 30.1, 27.8, 31.4, 29.0, 26.5, 32.2]   # list (data type) of 7 daily temperatures

total = 0                                     # running total starts at zero
for t in temps:                               # for loop: visit every temperature
    total = total + t                         # add it to the total
average = total / len(temps)                  # average = total / number of days
print("Average temperature:", round(average, 2), "C")   # round to 2 decimals for readability

i = 0                                         # while loop counter (index into the list)
hot_days = 0                                  # counts days warmer than average
while i < len(temps):                         # keep looping until the end of the list
    if temps[i] > average:                    # if-else: compare each day with the average
        hot_days = hot_days + 1               # count it
    i = i + 1                                 # move to the next day (prevents an endless loop)
print("Days above average:", hot_days, "of", len(temps))   # report the result
