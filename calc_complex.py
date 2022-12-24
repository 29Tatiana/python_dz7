def calc_comp(real1, real2, sign):
    if sign == '+':
        res = complex(real1.replace(' ', '')) + complex(real2.replace(' ', ''))
    elif sign == '-':
        res = complex(real1.replace(' ', '')) - complex(real2.replace(' ', ''))
    elif sign == '*':
        res = complex(real1.replace(' ', '')) * complex(real2.replace(' ', ''))
    else:
        res = complex(real1.replace(' ', '')) / complex(real2.replace(' ', ''))
    return res