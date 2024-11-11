def Fibonacci_series(terms):
    num1=0
    num2=1
    series=[num1,num2]
    for i in range(2,terms):
        num3= num1+num2
        series.append(num3)
        num1=num2
        num2=num3
    return series

n=19
res=Fibonacci_series(n)
print(res)

