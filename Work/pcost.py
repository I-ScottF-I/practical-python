# pcost.py
#
# Exercise 1.27
#
#Now that you know how to read a file, let’s write a program to perform a simple calculation.
#
#The columns in `portfolio.csv` correspond to the stock name, number of
#shares, and purchase price of a single stock holding.  Write a program called
#`pcost.py` that opens this file, reads all lines, and calculates how
#much it cost to purchase all of the shares in the portfolio.
#
#*Hint: to convert a string to an integer, use `int(s)`. To convert a string to a floating point, use `float(s)`.*
#
#Your program should print output such as the following:
#
#```bash
#Total cost 44671.15
#```

def portfolio_cost(file):
    cost = 0
    with open(file, 'rt') as dataSheet:
        next(dataSheet)
        for line in dataSheet:
            row = line.split(',')
            cost = cost + int(row[1]) * float(row[2])
    return cost

purchaseCost = portfolio_cost('Data/portfolio.csv')
print(purchaseCost)