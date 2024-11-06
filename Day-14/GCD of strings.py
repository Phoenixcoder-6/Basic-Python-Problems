import math
def gcd_string(str1,str2):
    if str1+str2==str2+str1:
        gcd_length= math.gcd(len(str1),len(str2))
        return str1[:gcd_length]
    

str1 = "ABCABC"
str2 = "ABC"
res= gcd_string(str1,str2)
print(res)