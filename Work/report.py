# report.py
#
# Exercise 2.4

import sys
import pprint
import csv
import string

def read_portfolio(file):
    #convert portfolio file into list of dicts
    portfolio = []
    with open(file, 'rt') as dataSheet:
        next(dataSheet)
        for line in dataSheet:
            row = line.split(',')
            d = {
                'name' : row[0],
                'shares': int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(d)
    return portfolio

def read_prices(file):
    #Read CSV and map into dict
    rowsNoBlanks = {}
    with open(file, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if not row == []:
                rowsNoBlanks[row[0]] = float(row[1])
    print
    return rowsNoBlanks

def make_report(currentPortfolio,currentPrice):
    report = []
    for item in currentPortfolio:
        diff = item['shares']*item['price']-item['shares']*currentPrice[item['name'].strip('"')]
        row = item['name'].strip('"'),item['shares'],item['price'],diff
        report.append(row)
    return report

#default filenames unless recieved as args
if len(sys.argv) == 3:
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
else:
    filename1 = 'Data/portfolio.csv'
    filename2 = 'Data/prices.csv'

#get vals
portfolioFull = read_portfolio(filename1)
prices = read_prices(filename2)

#find ROI
investment = 0.0
for item in portfolioFull:
    investment += item['shares'] * item['price']

currentValue = 0.0
for item in portfolioFull:
    currentValue += item['shares']* prices[item['name'].strip('"')]

print('Your portfolio cost: £',investment)
print('Your portfolio is worth: £',currentValue)
print('This portfolio has changed by: £',round((currentValue - investment),2)) 
#print nicely for debug
#pprint.pprint(portfolioFull)
#pprint.pprint(prices)

report = make_report(portfolioFull,prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
