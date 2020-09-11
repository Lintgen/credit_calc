import math
import sys
c_p = 0     # credit principal
n_p = 0     # number of payments
m_p = 0     # monthly payment
i = 0       # annual interest rate
total_dmp = 0   # total mth differentiated payment

args =sys.argv
c_par = ['--type', '--payment', '--principal', '--periods', '--interest']   # list of possible parameters

def parameters():   # function which reads parameters and asssigns its values to variables
    global c_p
    global n_p
    global m_p
    global i
    for ind, arg in enumerate(args[2:]):
        for par in c_par:
            if par in arg:
                if par == '--payment':
                    m_p = int(args[ind + 2][10:])
                if par == '--principal':
                    c_p = int(args[ind + 2][12:])
                elif par == '--periods':
                    n_p = int(args[ind + 2][10:])
                elif par == '--interest':
                    i = float(args[ind + 2][11:]) / (12 * 100)
                if c_p < 0 or n_p < 0 or i < 0:
                    print('Incorrect parameters')
                    exit()
def overpayment():
    return

if len(args) <= 4:
    print('Incorrect parameters')
    exit()

if args[1][7:] == 'diff':
    parameters()
    if m_p != 0:
        print('Incorrect parameters')
        exit()
    for per in range(1, n_p+1):
        dmp = (c_p / n_p) + i * (c_p - ((c_p * (per - 1)) / n_p))   # mth differentiated payment
        total_dmp += math.ceil(dmp)
        print(f'Month {per}: payment is {math.ceil(dmp)}')
    print('\nOverpayment = ', math.ceil(total_dmp - c_p))
elif args[1][7:] == 'annuity':
    parameters()
    if c_p != 0 and m_p != 0 and i !=0:
        n_p = int(math.ceil(math.log((m_p) / ((m_p) - i * c_p), 1 + i)))  # number of periods
        if n_p < 12:
            print(f'It will take {n_p} months to repay this credit!')
        elif n_p % 12 == 0:
            print(f'It will take {int(n_p / 12)} years to repay this credit!')
        else:
            print(f'It will take {int(n_p // 12)} years and {int(n_p % 12)} months to repay this credit!')
        print('Overpayment = ', n_p * m_p - c_p)
    elif c_p != 0 and n_p != 0 and i != 0:
        m_p = math.ceil(c_p * ((i * math.pow(1 + i, n_p)) / (math.pow(1 + i, n_p) - 1)))    # monthly payment
        print(f'Your annuity payment = {m_p}!')
        print('Overpayment = ', n_p * m_p - c_p)
    elif m_p != 0 and n_p != 0 and i != 0:
        c_p = int((m_p / ((i * math.pow(1 + i, n_p)) / (math.pow(1 + i, n_p) - 1))))    # credit principal
        print(f'Your credit principal = {c_p}!')
        print('Overpayment = ', n_p * m_p - c_p)
    else:
        print('Incorrect parameters')
        exit()