def occurance(string):
    freq={}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] =1


    return freq


string="ankitaGhosh"
print(occurance(string))