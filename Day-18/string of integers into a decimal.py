import decimal

def conv(string):
    dec= decimal.Decimal(string)
    return dec

s= '12345'
print(conv(s),type(conv(s)))