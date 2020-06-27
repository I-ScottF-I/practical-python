# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = int(input('What month will extra payments start in?'))
extra_payment_end_month = int(input('What month will extra payments end in?'))
extra_payment = int(input('How much extra is to be paid?'))
refund = 0


while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if months >= extra_payment_start_month and months < extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    months = months + 1
    print (months, total_paid, principal)

refund = abs(principal)
total_paid -= refund

print('Total paid in', months, 'months:', total_paid)
print('Refunded a total of', refund, 'for overpayments' )