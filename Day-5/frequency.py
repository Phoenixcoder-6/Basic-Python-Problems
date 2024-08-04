def find_frequency(string):
    freq={}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1   
    return freq

string= input()
res= find_frequency(string)
print(res)