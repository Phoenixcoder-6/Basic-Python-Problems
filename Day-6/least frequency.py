def least_frequency(string):
    freq={}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    least_freq= min(freq, key=freq.get)
    return least_freq

string= input("Enter the string:")
res= least_frequency(string)
print(res)