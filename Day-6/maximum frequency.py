import collections
def max_frequency(string):
    freq={}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    maximum= max(freq,key=freq.get)
    return maximum,freq

string= input("Enter the string:")
res= max_frequency(string)
print(res)
