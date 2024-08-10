marks= map(int,input(f"Enter the marks for 5 subjects:").split())
sum=0
for i in marks:
    sum= sum+i
per= (sum/500) * 100
print(per)

if per>90:
    print("Grade A")
elif per >70:
    print("Grade B")
elif per > 50:
    print("Grade C")
elif per>30:
    print("Grade D")
else:
    print ("Fail")