import decimal
def conv(integer):
    dec= decimal.Decimal(integer)
    return dec


num=10
print(conv(num),type(conv(num)))