stu=[]
n=int(input("Enter the range of the array:"))
for i in range(n):
    num=int(input(f"Enter the values at position {i+1}:"))
    stu.append(num)
print(stu)

grades= lambda number:['First' if (number>=90 and number<=100) else 'Second' if (number>=70 and number<=89) else 'Pass' for number in stu]
print(grades(stu))
