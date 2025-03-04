def occurance(string, char):
    count=0
    for i in string:
        if i== char:
            count+=1
    return count


string="ankitaa"
res= occurance(string,'a')
print(res)