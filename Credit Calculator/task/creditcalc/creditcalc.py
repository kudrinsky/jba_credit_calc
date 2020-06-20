import argparse
import sys
from math import log

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, help='type of payment')
parser.add_argument('--principal', type=float, help='credit principal')
parser.add_argument('--periods', type=int, help='count of months')
parser.add_argument('--payment', type=float, help='annuity payment')
parser.add_argument('--interest', type=float, help='credit interest')
credit = parser.parse_args()


def count_of_month():
    n_month = log(credit.payment / (credit.payment - interest * credit.principal), 1 + interest)
    if n_month > n_month // 1:
        n_month = n_month // 1 + 1

    year = int(n_month // 12)
    month = int(n_month % 12)
    period_y = ''
    period_m = ''
    if year == 1:
        period_y += '1 year'
    elif year > 1:
        period_y += str(year) + ' years'
    if month == 1:
        period_m = '1 month'
    elif month > 1:
        period_m = str(month) + ' months'
    if year != 0 and month != 0:
        period = period_y + ' and ' + period_m
    else:
        period = period_y + period_m
    print(f'You need {period} to repay this credit!')
    print(f'Overpayment = {int(n_month * credit.payment - credit.principal)}')


def a_payment():
    payment = credit.principal * (interest * (1 + interest) ** credit.periods) / ((1 + interest) ** credit.periods - 1)
    if payment > payment // 1:
        payment = int(payment // 1 + 1)
    print(f'Your annuity payment = {payment}!')
    print(f'Overpayment = {int(credit.periods * payment - credit.principal)}')


def c_principal():
    credit_principal = int(credit.payment / ((interest * (1 + interest) ** credit.periods) / (
                                                         (1 + interest) ** credit.periods - 1)))
    print(f'Your credit principal = {credit_principal}!')
    print(f'Overpayment = {int(credit.periods * credit.payment - credit_principal)}')


def diff_payment():
    summary = 0
    for i in range(1, credit.periods + 1):
        d_payment = credit.principal / credit.periods + interest * (credit.principal -
                                                                    (credit.principal * (i - 1)) / credit.periods)
        if d_payment > d_payment // 1:
            d_payment = d_payment // 1 + 1
        summary += d_payment
        print(f'Month {i}: paid out {round(d_payment)}')
    print()
    print(f'Overpayment = {int(summary - credit.principal)}')


if not credit.interest or len(sys.argv) < 5 or not credit.type \
        or (credit.type != 'diff' and credit.type != 'annuity') \
        or (credit.type == 'diff' and credit.payment) \
        or (credit.principal and credit.principal < 0) \
        or (credit.periods and credit.periods < 0) \
        or credit.interest < 0 or (credit.payment and credit.payment < 0):
    print('Incorrect parameters')
else:
    interest = credit.interest / 100 / 12
    if credit.type == 'diff':
        diff_payment()
    elif not credit.principal:
        c_principal()
    elif not credit.payment:
        a_payment()
    elif not credit.periods:
        count_of_month()
