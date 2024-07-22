T=(("arun",70),("barun",90),("jack",80))
print("All students : ",T)

R=()

for t in T:
    if(t[1]>=80):
        R+=(t,)

print("Students with score more than 80:",R)